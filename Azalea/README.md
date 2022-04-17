# Azalea
A simple, *somewhat* fast moderator tracker on any discord server.

<br>

## Configuration

###### Use environment variables!
###### Variables get converted to their required type on their own - no need to put quotation marks!
###### Mandatory environment variables are in **bold**.

<br>

#### Bot
| Variable | Description |
| - | - |
| **BOTTOKEN** | String, Bot token provided by discord |
| BOTPREFIX | String, Prefix for commands (default '>') |
| **CHANNELID** | Int, Channel where messages are sent to |

* Bot token can be found in the [Discord Developer Portal](https://discord.com/developers/applications).
* Channel ID can be found by right clicking on a channel and clicking copy ID.
 * This requires 'developer mode' to be enabled.

#### User

| Variable | Description |
| - | - |
| **USERTOKEN** | String, Token of a user |

* User's token can be found in application data, which is accessed via the developer console
 * If lost - google it
* User must be in the server which is stated in the Guild variable


#### Modwatching

| Variable  | Description |
| ------------- |:-------------:|
| AUTO      | Bool, Automatically determines moderator roles |
| **GUILD**      | String, Target guild (server) id     |
| MODROLES      | List(**String**), List of moderation roles needed to be tracked     |
| REFRESH | Float, amount of time to wait between checks.|

 * **ModRoles have to be filled if AUTO is set to False**
 * ModRoles are submitted as roleid;roleid;roleid
 * Refresh should be at least 4
 * AUTO is set to True by default
 
#### Misc
| Variable | Description |
| --------- | ----------- |
| DEBUG | Bool, prints and writes DEBUG output if True|
| LOGPATH | String, path for the log file |

* Debug is best presented as 1 for True and 0 for False
* LOGPATH Defaults to "./azalea.log" if its unable to write to stated path