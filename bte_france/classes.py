from dataclasses import dataclass
from enum import Enum
from typing import Union
import json

Y_OFFSET = 250  # For some unknown reason, Overviewer does not output markers on the correct y-coord, so we manually add an offset


class Type(str, Enum):
    BUILDING = "Bâtiments"
    CASTLE = "Châteaux"
    CHURCH = "Cathédrales & Eglises"
    CITY = "Villes"
    MONUMENT = "Monuments"
    PORT = "Ports"
    VILLAGE = "Villages"


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
    type: Type = None

    @property
    def poi_dict(self):
        return {"id": self.type, "text": self.name, "x": self.x, "y": self.y + Y_OFFSET, "z": self.z, "icon": f"icons/buildings/{self.type.name.lower()}.png"}

    def filter(self, poi):
        if poi["id"] == self.type or poi["id"] == "borders":
            return poi

    @property
    def marker_dict(self):
        if not self.type:
            raise Exception(f"Marker named {self.name} is missing a type!")
        return {
            "name": self.type.value,
            "filterFunction": self.filter,
            "checked": True,
            "showIconInLegend": True,
            "icon": f"icons/buildings/{self.type.name.lower()}.png"
        }

    @staticmethod
    def prefecture_dict():
        return {
            "name": "Préfectures",
            "filterFunction": lambda poi: poi if poi["id"] == "prefecture" else None,
            "checked": True,
            "showIconInLegend": True,
            "icon": "icons/buildings/prefecture.png"
        }


@dataclass
class Region:
    id: str
    name: str
    prefecture: Marker
    locations: list[Union[SquareLocation, RoundLocation]]
    markers: list[Marker]

    @property
    def prefecture_dict(self):
        return {"id": "prefecture", "text": self.prefecture.name, "x": self.prefecture.x, "y": self.prefecture.y + Y_OFFSET, "z": self.prefecture.z, "icon": f"icons/regions/{self.id}.png"}


def generate_borders() -> list[dict]:
    """Generate the borders of France and its regions"""
    borders_dict = {
        "regional": (1, "#8A8A8A"),
        "national": (2, "#D4D4D4")
    }

    borders = []
    for border_name, (weight, color) in borders_dict.items():
        with open(f"./bte_france/{border_name}_borders.json", 'r') as f:
            borders_json = json.load(f)

            for border in borders_json:
                polyline = []
                for x, z in border:
                    polyline.append({"x": x, "y": 0, "z": z})

                borders.append({"id": "borders", "x": 0, "y": 0, "z": 0, "polyline": polyline, "weight": weight, "color": color})

    return borders
