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
    try:
        acontent=str(iContent)
        utils.acontent = acontent
        utils.newLine=True
        utils.writeFile()
    except Exception as e:
        print(f"Error when writing the file. Error: {e}")

def wait5sec(utils):
    try:
        actual_ts=utils.Date2Timestamp()
        utils.timeStamp = actual_ts
        timeDiff = utils.TimestampTimeDiff()
        time.sleep(5)
        # while timeDiff < 5:
        #     time.sleep(0.1)
        #     wait5sec(utils)
    except Exception as e:
        print(f"Error when waiting to write. Error: {e}")

if __name__ == "__main__":
    try:
        iFile = "/opt/tmp/test.txt"
        #iFile=os.path.dirname(iFile)
        iContent = 0
        while iContent < 100:
            print(iContent)
            actual_date=datetime.now()
            utils = Utils(afile=iFile,fileMode="a",dateTime=actual_date)
            writeFile(utils)
            wait5sec(utils)
            iContent += 1
    except Exception as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        sys.exit("\n")
