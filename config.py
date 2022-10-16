from bte_france.classes import Marker, Region, generate_borders
from importlib import import_module
import shutil
import os


worlds["BTEFrance"] = "./worlds/CCMap"  # noqa
outputdir = "./outputs/BTEFranceMap"

# Create output directory
if not os.path.exists(outputdir):
    os.makedirs(outputdir)

# Copy icons to their appropriate directory
shutil.copytree("./bte_france/icons", f"{outputdir}/icons", dirs_exist_ok=True)

regions: list["Region"] = []
for file in os.listdir("./bte_france/regions"):
    if file.endswith(".py"):
        regions.append(getattr(import_module(f"bte_france.regions.{file[:-3]}"), "REGION"))

BTEcrop, manualpois, markers = [], [], [Marker.prefecture_dict()]
for region in regions:
    manualpois.append(region.prefecture_dict)

    for location in region.locations:
        BTEcrop.append(location.tuple)

    for marker in region.markers:
        manualpois.append(marker.poi_dict)
        markers.append(marker.marker_dict)
markers.sort(key=lambda marker_dict: marker_dict["name"])

renders["BTEFrance"] = {  # noqa
    "world": "BTEFrance",
    "title": "BTEFrance",
    "rendermode": normal,  # noqa
    "showspawn": False,
    "minzoom": 4,
    "showlocationmarker": False,
    "center": [2793842, -4798093],
    "BTEcrop": BTEcrop,
    "manualpois": manualpois + generate_borders(),
    "markers": markers
}
