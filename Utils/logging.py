from datetime import datetime
import pytz
from Variables.config import DEBUG, LOGPATH

def Log(type, log):
    UTC = pytz.utc
    types=["DEBUG", "LOG", "WARN", "ERROR", "FATAL"]
    CurTime=datetime.now(UTC)
    if DEBUG != True and type == 0:
        return
    try:
        with open(f"{LOGPATH}", "a+", encoding="utf-8") as filewrite:
            filewrite.write(f"[{CurTime}] [{types[type]}]: {log}\n")
    except:
        with open(f"./azalea.log", "a+", encoding="utf-8") as filewrite:
            filewrite.write(f"[{CurTime}] [{types[type]}]: {log}\n")
    print(f"[{CurTime}] [{types[type]}]: {log}")