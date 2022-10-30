from importlib import import_module
from dataclasses import dataclass
from enum import Enum
from typing import Union
import json
import os

Y_OFFSET = 250  # For some unknown reason, Overviewer does not output markers on the correct y-coord, so we manually add an offset


class Type(str, Enum):
    BUILDING = "Bâtiments"
    CASTLE = "Châteaux"
    CHURCH = "Edifices Religieux"
    CITY = "Villes"
    MONUMENT = "Monuments"
    PORT = "Ports"
    VILLAGE = "Villages"
    LIGHTHOUSE = "Phares"


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
        return {"id": self.type.name.lower(), "text": self.name, "x": self.x, "y": self.y + Y_OFFSET, "z": self.z, "icon": f"icons/buildings/{self.type.name.lower()}.png"}

    def filter(self, poi):
        if poi["id"] == self.type.name.lower() or poi["id"] == "borders":
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
            "filterFunction": lambda poi: poi if poi["id"] == "prefecture" or poi["id"] == "borders" else None,
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


@dataclass
class World:
    id: str
    name: str
    regions: list[str]
    center: tuple[int, int]
    minzoom: int

    def __post_init__(self):
        self._BTEcrop, self._manualpois, self._markers = [], [], [Marker.prefecture_dict()]
        for region in REGIONS:
            if region.id in self.regions:
                self._manualpois.append(region.prefecture_dict)

            if self.id == "france":
                for location in region.locations:
                    self._BTEcrop.append(location.tuple)

            if region.id in self.regions:
                for marker in region.markers:
                    self._manualpois.append(marker.poi_dict)
                    self._markers.append(marker.marker_dict)
        self._markers.sort(key=lambda marker_dict: marker_dict["name"])

        if self.id == "france":
            self._manualpois += generate_borders("national") + generate_borders("regional")
        else:
            self._manualpois += generate_borders("outre_mer")

    @property
    def dict(self):
        return {
            "world": self.name,
            "title": self.name,
            "rendermode": "normal",
            "showspawn": False,
            "minzoom": self.minzoom,
            "showlocationmarker": False,
            "center": self.center,
            "BTEcrop": self._BTEcrop,
            "manualpois": self._manualpois,
            "markers": self._markers,
            "texturepath": "/home/maxyolo01/.minecraft/versions/1.16/1.16.jar",
        }


def generate_borders(border: str) -> list[dict]:
    """Generate the borders of France and its regions"""
    borders_dict = {
        "regional": (1, "#8A8A8A"),
        "national": (2, "#D4D4D4"),
        "outre_mer": (1, "#8A8A8A")
    }

    borders = []
    weight, color = borders_dict[border]
    with open(f"./bte_france/{border}_borders.json", 'r') as f:
        borders_json = json.load(f)

        for border in borders_json:
            polyline = []
            for x, z in border:
                polyline.append({"x": x, "y": 0, "z": z})

            borders.append({"id": "borders", "x": 0, "y": 0, "z": 0, "polyline": polyline, "weight": weight, "color": color})

    return borders


REGIONS: list[Region] = []
for file in os.listdir("./bte_france/regions"):
    if file.endswith(".py"):
        REGIONS.append(getattr(import_module(f"bte_france.regions.{file[:-3]}"), "REGION"))
