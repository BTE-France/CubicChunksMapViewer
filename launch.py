import os

for location_file in os.listdir("./locations"):
    os.system(f"python.exe overviewer.py --config=config.py --forcerender {location_file}")
