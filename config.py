from bte_france.worlds import WORLDS
import shutil
import os


inputdir = "./worlds/CCMap"
outputdir = "./outputs/BTEFranceMap"

# Create output directory
if not os.path.exists(outputdir):
    os.makedirs(outputdir)

# Copy icons to their appropriate directory
shutil.copytree("./bte_france/icons", f"{outputdir}/icons", dirs_exist_ok=True)

for world in WORLDS:
    worlds[world.name] = inputdir  # noqa
    renders[world.id] = world.dict  # noqa
