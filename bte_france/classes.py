from typing import Union
from dataclasses import dataclass


@dataclass
class SquareLocation:
    x_min: int
    z_min: int
    x_max: int
    z_max: int
    y_min: int = None
    y_max: int = None

    @property
    def tuple(self):
        return (self.x_min, self.z_min, self.x_max, self.z_max, self.y_min if self.y_min else -100, self.y_max if self.y_max else 5000)


@dataclass
class RoundLocation:
    x: int
    z: int
    radius: int
    y_min: int = None
    y_max: int = None

    @property
    def tuple(self):
        return (self.x, self.z, self.radius, self.y_min if self.y_min else -100, self.y_max if self.y_max else 5000)


@dataclass
class Marker:
    name: str
    x: int
    y: int
    z: int
    region: str = None

    @property
    def dict(self):
        return {"id": self.region, "name": self.name, "x": self.x, "y": self.y + 780, "z": self.z, "icon": f"icons/{self.region}.png"}


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
        if poi["id"] == self.id:
            return poi["name"]

    @property
    def markers_dict(self):
        return {
            "name": self.name,
            "filterFunction": self.filter,
            "checked": True,
            "showIconInLegend": True,
            "icon": f"icons/{self.id}.png"
        }
