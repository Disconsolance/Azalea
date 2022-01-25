# Azalea
A simple, *somewhat* fast moderator tracker on any discord server.

<br>

## Configuration

**Copy config.py.example to config.py<br>**

#### Bot
| Variable | Description |
| - | - |
| BOTTOKEN | String, Bot token provided by discord |
| BOTPREFIX | String, Prefix for commands (default '>') |
| CHANNELID | Int, Channel where messages are sent to |

* Bot token can be found in the [Discord Developer Portal](https://discord.com/developers/applications).
* Channel ID can be found by right clicking on a channel and clicking copy ID.
 * This requires 'developer mode' to be enabled.

#### User

| Variable | Description |
| - | - |
| USERTOKEN | String, Token of a user |

* User's token can be found in application data, which is accessed via the developer console
 * If lost - google it
* User must be in the server which is stated in the Guild variable


#### Modwatching

| Variable  | Description |
| ------------- |:-------------:|
| AUTO      |Bool, Automatically determines moderator roles |
| Guild      | String, Target guild (server) id     |
| ModRoles      | List(**String**), List of moderation roles needed to be tracked     |
| Refresh | Float, amount of time to wait between checks.|

 * ModRoles have to be filled if AUTO is set to False
 * Refresh should be at least 3
 
#### Misc
| Variable | Description |
| --------- | ----------- |
| DEBUG | Bool, prints and writes DEBUG output if True|
| LOGPATH | String, path for the log file |

* LOGPATH Defaults to "./azalea.log" if its unable to write to stated path