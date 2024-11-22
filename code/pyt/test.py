#!/usr/bin/python3

import sys
import os
from datetime import datetime
import time

try:
    # # Add the directory to the system path
    # script_dir = os.path.dirname(os.path.abspath(__file__))
    # utils_dir = os.path.abspath(os.path.join(script_dir, "../../Python-Utils"))
    # sys.path.append(utils_dir)

    # # Now import the file
    # from utils import Utils

    # Import the module
    sys.path.append(os.path.dirname("/opt/dev/Python-Utils/utils.py"))
    from utils import Utils
except Exception as e:
    print(e)
    sys.exit()

def writeFile(utils):
    write2file = utils.writeFile()

def wait5sec(utils):
    actual_ts=utils.Date2Timestamp()
    utils = Utils(timeStamp=actual_ts)
    timeDiff = utils.TimestampTimeDiff()
    while timeDiff < 5:
        wait5sec(utils)
        time.sleep(0.1)

if __name__ == "__main__":
    iFile = "../../src/test.txt"
    iContent = 0
    while iContent < 100:
        actual_date=datetime.now()
        utils = Utils(afile=iFile,acontent=str(iContent),fileMode="a",newLine=True,dateTime=actual_date)
        writeFile(utils)
        wait5sec(utils)
        iContent += 1
