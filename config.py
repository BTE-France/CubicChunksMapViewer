from bte_france.worlds import WORLDS
import shutil
import json
import os


with open("./settings.json", "r") as f:
    settings = json.load(f)
    inputdir = settings["WORLD_INPUT"]
    outputdir = settings["WORLD_OUTPUT"]

# Create output directory
if not os.path.exists(outputdir):
    os.makedirs(outputdir)

# Copy icons to their appropriate directory
shutil.copytree("./bte_france/icons", f"{outputdir}/icons", dirs_exist_ok=True)

for world in WORLDS:
    worlds[world.name] = inputdir  # noqa
    renders[world.id] = world.dict  # noqa
