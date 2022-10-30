import subprocess
import time
import os

PYTHON_EXECUTABLE = "python3.9" if os.name == "posix" else "python.exe"

try:
    start = time.time()
    subprocess.run(f"{PYTHON_EXECUTABLE} overviewer.py --config=config.py --forcerender".split(), check=True)
    end = time.time()
    subprocess.run(f"{PYTHON_EXECUTABLE} overviewer.py --config=config.py --genpoi --skip-players --skip-scan".split(), check=True)
    print(f"Map was succesfully generated in {time.strftime('%H hour(s), %M minute(s) and %S second(s)', time.gmtime(end - start))}")
except subprocess.CalledProcessError:
    print("An error was encountered while generating the map!")
except KeyboardInterrupt:
    print("Map generation manually halted.")
