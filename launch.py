import subprocess
import time

try:
    start = time.time()
    subprocess.run("sudo python3.9 overviewer.py --config=config.py --forcerender".split(), check=True)
    subprocess.run("sudo python3.9 overviewer.py --config=config.py --genpoi --skip-players --skip-scan".split(), check=True)
    end = time.time()
    print(f"Map was succesfully generated in {time.strftime('%H hour(s), %M minute(s) and %S second(s)', time.gmtime(end - start))}")
except subprocess.CalledProcessError:
    print("An error was encountered while generating the map!")
except KeyboardInterrupt:
    print("Map generation manually halted.")
