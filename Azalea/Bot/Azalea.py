import discum
from discord.ext import commands
import time
import subprocess
import asyncio
import os
import Variables.config
from Bot.vars import *
from Utils.environment import FillConfig
from Utils.lists import *
from Utils.logging import *
from Objects.Mod import Moderator

User = discum.Client(token=os.getenv('USERTOKEN'))
User.gateway.log = {"console":False, "file":False}
User.log = {"console":False, "file":False}
Bot = commands.Bot(command_prefix=os.getenv('BOTPREFIX'), case_insensitive=True)



@User.gateway.command
def Bloom(resp):
	if resp.event.ready_supplemental:
		User.gateway.checkGuildMembers(Variables.config.Guild, List, keep="all")
	if resp.event.guild_members_chunk and User.gateway.finishedGuildSearch(Variables.config.Guild, userIDs=List):
		User.gateway.close()

@Bot.event
async def on_ready():
    global User
    User.gateway.run()
    await FillModStatus()
    asyncio.get_event_loop().create_task(Ping())

@Bot.command(name="status", brief="Fetches total amount of online moderators")
async def Status(ctx):
    i = 0
    for Jannie in Jannies:
        if Jannie.Status != "offline":
            i+=1
    
    string=""
    if i == 0:
        string="There are no currently online moderators."
    elif i == 1:
        string="There is only 1 online moderator."
    else:
        string=f"There are {i} currently online moderators"

    await Notify(string)

@Bot.command(name="forceupdate")
async def CallUpdate(ctx):
    await Update()

@Bot.command(name="version")
async def GetHash(ctx):
    await Notify(f"The current commit hash is {subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']).decode('ascii').strip()}.")

async def UpdateRole(index):
    global UserIDList
    UserIDList[index] = Filter(User.getRoleMemberIDs(Variables.config.Guild, ModRoles[index]).content.decode())
    Log(0, f"Now - {UserIDList[index]}")
    # TODO: Update trackerlist

async def Update():
    Counters = dict(json.loads(User.getRoleMemberCounts(Variables.config.Guild).content.decode()))
    for i in range(len(ModRoles)):
        if len(UserIDList[i]) != Counters[ModRoles[i]]:
            Log(0, f"Members in {ModRoles[i]} have changed!\nWas: {UserIDList[i]}")
            await UpdateRole(i)

async def Notify(message):
	channel = Bot.get_channel(Variables.config.CHANNELID)
	await channel.send(message)

async def Ping():
    while True:
        Log(0, "Bloom")
        User.gateway.run()
        for i in range(len(List)):
            try:
                what = User.gateway.session.guild(Variables.config.Guild).members[List[i]]
                tmp = GetObject(what)
                if tmp.Status != Jannies[i].Status:
                    Log(1, f"{tmp.Username} ({tmp.Identity}) changed status to {tmp.Status}. Previously was {Jannies[i].Status}. {(tmp.Timestamp-Jannies[i].Timestamp)} has elapsed.")
                    Jannies[i] = tmp
                    await Notify(f"{tmp.Username} ({tmp.Identity}) is now {tmp.Status}")
                await asyncio.sleep(Variables.config.Refresh)
            except KeyError:
                Log(1, f"Cant find {Jannies[i].Username}! Removing from list!")
                List.pop(i)
                Jannies.pop(i)


def FillLists():
    global List
    global ModRoles
    global Roles
    global UserIDList
    List=[]
    UserIDList=[]

    # Get all current roles on a server
    print("Stage 0: Fetching roles")
    Roles = SortRoles(User.getGuildRoles(Variables.config.Guild).content.decode())
    
    # Automatic moderator fetching
    if Variables.config.AUTO == True:
        ModRoles=[] # Reset list just in case
        Roles = SortRoles(User.getGuildRoles(Variables.config.Guild).content.decode())
        print("Stage 1: Filtering moderators")
        for i in range(len(Roles)):
            if (CheckJanitorPerms(int(Roles[i]["permissions"])) == True):
                ModRoles.append(Roles[i]["id"])
    Log(0, f"Got {len(ModRoles)} moderator roles")
    for RoleId in ModRoles:
        Log(0, f"Getting UserID's for {RoleId}")
        UserIDs = Filter(User.getRoleMemberIDs(Variables.config.Guild, RoleId).content.decode())
        Log(0, f"Fetched {UserIDs}")
        UserIDList.append(UserIDs)
        time.sleep(5)

    # Flatten list
    FlattenedUserIDList = [j for sub in UserIDList for j in sub]
    # Append to list if not already in the list, removing duplicates
    [List.append(x) for x in FlattenedUserIDList if x not in List]

    # Exit if List is empty
    if len(List) == 0:
        Log(4, "List is empty! Check Role IDs!")
        exit(1)

async def FillModStatus():
    print("Stage 2: Filling mod status")
    for i in range(len(List)):
        Janny = User.gateway.session.guild(Variables.config.Guild).members[List[i]]
        Obj = GetObject(Janny)
        Jannies.append(Obj)
        Log(0, f"Queried {i}, got \"{Obj.Username} ({Obj.Identity}) is {Obj.Status}\"")
        await Notify(f"{Obj.Username}, ({Obj.Identity}) is {Obj.Status}")
        time.sleep(0.8)
    await Notify(f"Azalea started - tracking {len(List)} moderators total.")

def Init():
    FillLists()
    Kickstart()

def Kickstart():
    Bot.run(Variables.config.BOTTOKEN)


