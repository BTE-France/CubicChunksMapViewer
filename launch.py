import subprocess

subprocess.run("sudo python3 overviewer.py --config=config.py --forcerender".split())
subprocess.run("sudo python3 overviewer.py --config=config.py --genpoi --skip-players --skip-scan".split())
