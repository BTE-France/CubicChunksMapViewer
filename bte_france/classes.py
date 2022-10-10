from dataclasses import dataclass
from typing import Union
import json


@dataclass
class SquareLocation:
    x1: int
    z1: int
    x2: int
    z2: int
    y_min: int = -100
    y_max: int = 5000

    @property
    def tuple(self):
        return (self.x1, self.z1, self.x2, self.z2, self.y_min, self.y_max)


@dataclass
class RoundLocation:
    x: int
    z: int
    radius: int
    y_min: int = -100
    y_max: int = 5000

    @property
    def tuple(self):
        return (self.x, self.z, self.radius, self.y_min, self.y_max)


@dataclass
class Marker:
    name: str
    x: int
    y: int
    z: int
    region: str = None

    @property
    def dict(self):
        return {"id": self.region, "text": self.name, "x": self.x, "y": self.y + 780, "z": self.z, "icon": f"icons/{self.region}.png"}


@dataclass
class Region:
    id: str
    name: str
    locations: list[Union[SquareLocation, RoundLocation]]
    markers: list[Marker]

    def __post_init__(self):
        for marker in self.markers:
            marker.region = self.id

    def filter(self, poi):
        if poi["id"] == self.id or poi["id"] == "borders":
            return poi

    @property
    def markers_dict(self):
        return {
            "name": self.name,
            "filterFunction": self.filter,
            "checked": True,
            "showIconInLegend": True,
            "icon": f"icons/{self.id}.png"
        }


def generate_borders() -> list[dict]:
    """Generate the borders of France"""
    borders = []
    with open("./bte_france/borders.json", 'r') as f:
        borders_json = json.load(f)

        for border in borders_json:
            polyline = []
            for x, z in border:
                polyline.append({"x": x, "y": 0, "z": z})

            borders.append({"id": "borders", "x": 0, "y": 0, "z": 0, "polyline": polyline})
    return borders
