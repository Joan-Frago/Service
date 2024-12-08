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
    sys.path.insert(0,"../../../Python-Utils/utils/")
    from utils import *
except Exception as e:
    print(e)
    sys.exit()

def write2File(aFile,aContent):
    try:
        writeFile(aFile=aFile,aContent=str(aContent),newLine=True)
    except Exception as e:
        print(f"Error when writing the file. Error: {e}")

def wait5sec():
    Actual_date=datetime.now()
    try:
        actual_ts=Date2Timestamp(Actual_date)
        timeDiff = TimestampTimeDiff(actual_ts)
        time.sleep(5)
    except Exception as e:
        print(f"Error when waiting to write. Error: {e}")

if __name__ == "__main__":
    try:
        iFile = "/opt/tmp/test.txt"
        #iFile=os.path.dirname(iFile)
        iContent = 0
        while iContent < 100:
            print(iContent)
            write2File(iFile,iContent)
            wait5sec()
            iContent += 1
    except Exception as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        sys.exit("\n")
