import os
import sys
import time
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

files = os.listdir("./downloads")

try:
    if files:
        time.sleep(60 * 60 * 2)
        for f in files:
            os.remove(str("./downloads/" + f))
except Exception as e:
    print("Exception cleaning up files: ", e)
