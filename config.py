from typing import TYPE_CHECKING
from importlib import import_module
import os

if TYPE_CHECKING:
    from bte_france.classes import Region


def poiFilter(poi):
    if poi["id"]:
        return poi['name']


worlds["BTEFrance"] = "./worlds/CCMap"

regions: list["Region"] = []
for file in os.listdir("./bte_france/regions"):
    if file.endswith(".py"):
        regions.append(getattr(import_module(f"bte_france.regions.{file[:-3]}"), "REGION"))

renders["BTEFrance"] = {
    "world": "BTEFrance",
    "title": "BTEFrance",
    "rendermode": normal,
    "showspawn": False,
    "BTEcrop": [location.tuple for region in regions for location in region.locations],
    "manualpois": [marker.dict for region in regions for marker in region.markers],
    "markers": [region.markers_dict for region in regions]
}

outputdir = "./outputs/BTEFranceMap"
