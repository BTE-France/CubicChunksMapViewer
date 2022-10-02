import subprocess
import time

start = time.time()
end = time.time()
print(f"Map was succesfully generated in {time.strftime('%H hour(s), %M minute(s) and %S second(s)', time.gmtime(end - start))}")
