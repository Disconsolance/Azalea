from datetime import datetime
import pytz
import Variables.config

def Log(type, log):
    UTC = pytz.utc
    types=["DEBUG", "LOG", "WARN", "ERROR", "FATAL"]
    CurTime=datetime.now(UTC)
    if Variables.config.DEBUG != True and type == 0:
        return
    try:
        with open(f"{Variables.config.LOGPATH}", "a+", encoding="utf-8") as filewrite:
            filewrite.write(f"[{CurTime}] [{types[type]}]: {log}\n")
    except:
        with open(f"./azalea.log", "a+", encoding="utf-8") as filewrite:
            filewrite.write(f"[{CurTime}] [{types[type]}]: {log}\n")
    print(f"[{CurTime}] [{types[type]}]: {log}")