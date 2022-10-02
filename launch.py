import subprocess
import time

start = time.time()
subprocess.run("sudo python3.9 overviewer.py --config=config.py --forcerender".split())
subprocess.run("sudo python3.9 overviewer.py --config=config.py --genpoi --skip-players --skip-scan".split())
end = time.time()
print(f"Map was succesfully generated in {time.strftime('%H hour(s), %M minute(s) and %S second(s)', time.gmtime(end - start))}")
