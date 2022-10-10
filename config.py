from bte_france.classes import Region, generate_borders
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

renders["BTEFrance"] = {  # noqa
    "world": "BTEFrance",
    "title": "BTEFrance",
    "rendermode": normal,  # noqa
    "showspawn": False,
    "minzoom": 3,
    "showlocationmarker": False,
    "center": [2793842, -4798093],
    "BTEcrop": [location.tuple for region in regions for location in region.locations],
    "manualpois": [marker.dict for region in regions for marker in region.markers] + generate_borders(),
    "markers": [region.markers_dict for region in regions]
}
