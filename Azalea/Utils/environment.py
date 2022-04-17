from Variables import config
import os

def FillConfig():
    # Mandatory
    if all(v is not None for v in [os.getenv('BOTTOKEN'), os.getenv('USERTOKEN'), os.getenv('CHANNELID'), os.getenv('GUILD')]):
        config.BOTTOKEN = os.getenv('BOTTOKEN')
        config.USERTOKEN = os.getenv('USERTOKEN')
        config.CHANNELID = os.getenv('CHANNELID')
        config.Guild = os.getenv('GUILD')
    else:
        raise AttributeError

    #Optional
    if os.getenv('REFRESH') is not None:
        config.Refresh = int(os.genenv('REFRESH'))
    if os.getenv('REFRESH') is not None:
        config.AUTO = bool(os.getenv('AUTO'))
    if os.getenv('DEBUG') is not None:
        config.DEBUG = bool(os.getenv('DEBUG'))
    if os.getenv('BOTPREFIX') is not None:
        config.BOTPREFIX = os.getenv('BOTPREFIX')
    if os.getenv('LOGPATH') is not None:
        config.LOGPATH = os.getenv('LOGPATH')

    # Mandatory if AUTO is set to false
    if bool(os.getenv('AUTO')) is False:
        config.ModRoles = str(os.getenv('MODROLES')).split(';')