import Variables.config
import os

def FillConfig():
    # Mandatory
    if all(v is not None for v in [os.getenv('BOTTOKEN'), os.getenv('USERTOKEN'), os.getenv('CHANNELID'), os.getenv('GUILD')]):
        Variables.config.BOTTOKEN = os.getenv('BOTTOKEN')
        Variables.config.USERTOKEN = os.getenv('USERTOKEN')
        Variables.config.CHANNELID = int(os.getenv('CHANNELID'))
        Variables.config.Guild = os.getenv('GUILD')
    else:
        raise AttributeError

    #Optional
    if os.getenv('REFRESH') is not None:
        Variables.config.Refresh = int(os.genenv('REFRESH'))
    if os.getenv('REFRESH') is not None:
        Variables.config.AUTO = bool(os.getenv('AUTO'))
    if os.getenv('DEBUG') is not None:
        Variables.config.DEBUG = bool(os.getenv('DEBUG'))
    if os.getenv('BOTPREFIX') is not None:
        Variables.config.BOTPREFIX = os.getenv('BOTPREFIX')
    if os.getenv('LOGPATH') is not None:
        Variables.config.LOGPATH = os.getenv('LOGPATH')

    # Mandatory if AUTO is set to false
    if bool(os.getenv('AUTO')) is False:
        Variables.config.ModRoles = str(os.getenv('MODROLES')).split(';')