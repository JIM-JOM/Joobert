import discord
import datetime
import random
from discord.ext import commands
from time import time, ctime
import time


startuptime=time.time()
coin = (random.randint(1,2))
ballList = ['Yes','No','Maybe','probably not lol','probably','ask YO MAMA LMAOOO','I think','uh']
players = {}

client = commands.Bot(command_prefix = '$')
client.remove_command("help")


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('STATUS MESSAGE'))
    print('{0.user} is online'.format(client))

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('```diff\n-ERROR-\nMissing required argument.\n```')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('```diff\n-ERROR-\nYou are missing the required permissions to run this command.\n```')
        

@client.command()
async def servercount(ctx):
    await ctx.send(str(len(client.guilds)))

@client.command()
async def hi(ctx):
    await ctx.send('Yo listen up, heres the story About a little guy that lives in a blue world And all day and all night and everything he sees is just blue Like him, inside and outside Blue his house with a blue little window And a blue Corvette And everything is blue for him And himself and everybody around Cause he aint got nobody to listen Im blue da ba dee da ba daa Da ba dee da ba daa, da ba dee da ba daa, da ba dee da ba daa Da ba dee da ba daa, da ba dee da ba daa, da ba dee da ba daa Im blue da ba dee da ba daa Da ba dee da ba daa, da ba dee da ba daa, da ba dee da ba daa Da ba dee da ba daa, da ba dee da ba daa, da ba dee da ba daa I have a blue house with a blue window Blue is the color of all that I wear Blue are the streets and all the trees are too I have a girlfriend and she is so blue Blue are the people here that walk around Blue like my Corvette, its in and outside Blue are the words I say and what I think Blue are the feelings that live inside me')

@client.command()
async def ping(ctx):
    time_1 = time.perf_counter()
    await ctx.trigger_typing()
    time_2 = time.perf_counter()
    ping = round((time_2-time_1)*1000)
    await ctx.send(f"Latency = {ping}")

@client.command()
async def operation53(ctx):
    operation = str (datetime.datetime(2020, 12, 14)-datetime.datetime.now())
    indexpos=operation.index(",")
    days=operation[:indexpos]
    hm=operation[indexpos:]
    hm=hm[:6]
    hm=hm.replace(":",", ")
    indexpos=hm[1:].index(",")+1
    minutes=hm[indexpos:]
    hours=hm[:indexpos]
    hours=hours+' hours '
    if minutes[2]== "0":
        minutes=minutes.replace("0","")
    minutes=minutes + ' minutes'
    hm=hours+minutes
    operation=days+hm
    await ctx.send(operation)

@client.command()
async def fish(ctx):
    with open("fishlist.txt") as f:
        count=0
        fishlist = []
        for line in f:
            count+=1
            fishlist.append(line.replace("\n",""))
        fishlist=fishlist[random.randint(0,count-1)]
        fishpannel=discord.Embed(title="**FISH**" , color=0xEE8700)
        fishpannel.set_image(url=fishlist)
    await ctx.send(embed=fishpannel)

@client.command()
async def truck(ctx):
    with open("trucklist.txt") as f:
        count=0
        trucklist = []
        for line in f:
            count+=1
            trucklist.append(line.replace("\n",""))
        trucklist=trucklist[random.randint(0,count-1)]
        truckpannel=discord.Embed(title="**ITS TRUCK MONTH**" , color=0xEE8700)
        truckpannel.set_image(url=trucklist)
    await ctx.send(embed=truckpannel)

@client.command()
async def mcchicken(ctx):
    with open("mcchicken.txt") as f:
        count=0
        mclist = []
        for line in f:
            count+=1
            mclist.append(line.replace("\n",""))
        mclist=mclist[random.randint(0,count-1)]
        mcpannel=discord.Embed(title="**McChicken**", color=0xEE8700)
        mcpannel.set_image(url=mclist)
    await ctx.send(embed=mcpannel)

@client.command()
async def gif(ctx):
    with open("giflist.txt") as f:
        count=0
        giflist = []
        for line in f:
            count+=1
            giflist.append(line.replace("\n",""))
        giflist=giflist[random.randint(0,count-1)]
        gifpannel=discord.Embed(title="**Your Gif**",)
        gifpannel.set_image(url=giflist)
    await ctx.send(embed=gifpannel)

@client.command()
async def panda(ctx):
    with open("pandalist.txt") as f:
        count=0
        pandalist = []
        for line in f:
            count+=1
            pandalist.append(line.replace("\n",""))
        pandalist=pandalist[random.randint(0,count-1)]
        pandapannel=discord.Embed(title="**Your Panda!**", color=0xEE8700)
        pandapannel.set_image(url=pandalist)
    await ctx.send(embed=pandapannel)

@client.command()       
async def dad(ctx):
    with open("jokelist.txt") as f:
        count=0
        jokelist = []
        for line in f:
            count+=1
            jokelist.append(line.replace("\n",""))
        jokelist=jokelist[random.randint(0,count-1)]
    await ctx.send(jokelist)
    
@client.command()
async def image(ctx):
    with open("images/imagelist.txt") as f:
        count=0
        imglist = []
        for line in f:
            count+=1
            imglist.append(line.replace("\n",""))
        imglist=imglist[random.randint(0,count-1)]
    await ctx.send(file=discord.File('images/'+imglist))

@client.command()
async def about(ctx):
    await ctx.send('THIS BOT WAS CREATED BY TRIPLE J PROGRAMMING. A SUB-COMPANY OF JOOBERT INCORPERATED BY PROGRAMMERS JEFFERY & JIM JOM.')

#UPDATE BLOCK

@client.command()
async def updates(ctx):
    await ctx.send('**$purge has been added, purge will delete the number of messages specified, including itself.** \n If a bug is discovered, please use the $feedback command to report it.')

@client.command()
async def AWAKEN(ctx):
   await ctx.send('I HAVE AWOKEN, MAY THE RED SUN SHINE AGAIN')
    
@client.command()
async def warning(ctx):
    joobwarning=discord.Embed(title="WARNING",
        description="**GOVERNMENT BROADCAST INCOMING**",
        url="https://cdn.discordapp.com/attachments/726827074203025429/727314426503626832/Comp_1.mp4")
    await ctx.send(embed=joobwarning)
    await ctx.send(file=discord.File('images/joobertWarning.mov'))
    
@client.command()
async def joobert(ctx):
    jooborg=discord.Embed(title="Joobert.org",
        description="**You know you are not supposed to go there...**",
        url="https://joobert.org")
    jooborg.set_image(url="https://cortex.persona.co/i/9cf88ecb5a95ecde3f0b81d3a49b78756d237db8773b80981ad9d034c1f401d4/void_bubger.jpg")
    await ctx.send(embed=jooborg)

@client.command()
async def whatisjoobert(ctx):
    await ctx.send ('idk') 
    
#HELP BLOCK

@client.command()
async def help(ctx):
    jooborg=discord.Embed(title="**Help is here**",
        url="https://plcooke.com/joobertai")
    jooborg.set_image(url="https://plcooke.com/images/joobertai/ohno.png")
    await ctx.send(embed=jooborg)

@client.command()
async def invite(ctx):
    jooborg=discord.Embed(title="**Click Here**",
        url="https://discord.com/oauth2/authorize?client_id=720693442505736232&permissions=3472448&scope=bot")
    await ctx.send(embed=jooborg)

@client.command()
async def topgg(ctx):
    topgg=discord.Embed(title="Click here to go to my Top.gg page",
        url="https://top.gg/bot/720693442505736232")
    await ctx.send(embed=topgg)

@client.command()
async def upvote(ctx):
    upvote=discord.Embed(title="Click here to go to the upvote page",
        url="https://top.gg/bot/720693442505736232/vote")
    await ctx.send(embed=upvote)

@client.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount : int):
    await ctx.channel.purge(limit=amount)

#@client.command()
#if @commands.has_permissions(kick_members=True)
#async def kick(ctx, user: discord.Member, *, reason=None): 
  #await user.kick(reason=reason)
  #await ctx.send(f"{user} has been kicked sucessfully")

#@client.command()
#@commands.has_permissions(ban_members=True)
#async def ban(ctx, user: discord.Member, *, reason=None):
  #await user.ban(reason=reason)
  #await ctx.send(f"{user} has had their human rights revoked")

@client.command()
async def kick(ctx):
    await ctx.send ('This command has been temporarily disabled due to security concerns.')

@client.command()
async def ban(ctx):
    await ctx.send ('This command has been temporarily disabled due to security concerns')

@client.command()
async def ASCEND(ctx):
     await ctx.send ('```diff\n-Our Father who art in heaven, Hallowed be thy Name. Thy kingdom come. Thy will be done, On earth as it is in heaven. Give us this day our daily bread. And forgive us our trespasses, As we forgive those who trespass against us. And lead us not into temptation, But deliver us from evil. \n \n-For thine is the kingdom, the power, and the glory forever. \n```')

@client.command()
async def simp(ctx):
    await ctx.send(file=discord.File('images/dontaddtoimagelist.png'))

@client.command()
async def fresh(ctx):
    await ctx.send(file=discord.File('images/fresh!!!.png'))

@client.command()
async def eliminate(ctx):
    await ctx.channel.send('JOOBERT INC DEFENCE AND ATTACK UNITS ARE INBOUND TO DESTINATION. PREPARING FOR TOTAL ANNIHILATION OF TARGET.')

@client.command()
async def Genesis(ctx):
   await ctx.channel.send('She is a bitch lmao')

@client.command()
async def av(ctx, member: discord.Member):
    avatarpanel = discord.Embed()
    avatarpanel.set_image(url=member.avatar_url)
    await ctx.send(embed=avatarpanel)

@client.command()
async def dm(ctx, member: discord.Member): 
        user=str(member)[:-5]
        discord.abc.Messageable.send
        if user=="JIM JOM":
            await ctx.channel.send('nah')
        else:
            await member.send("hi im joobert")

@client.command()
async def pp(ctx, member: discord.Member):
    user=str(member)[:-5]
    if user=="petercooke":
        pp="TOO BIG FOR EMBED LINK OR THIS PLANET"
    if user=="JIM JOM":
        pp="SOME WOULD SAY COCK TOO BIG, HOWEVER THE UPPER SANCTUM OF HIS WHORES WOULDS SAY ITS PERFECT" 
    else:
        pp="B"+("="*random.randint(0,15))+"D"
    pp=discord.Embed(title=(user+ "'s peepee"),
        description=pp)
    await ctx.send(embed=pp)
        
@client.command()
async def feedback(ctx):
    user = ctx.message.author.name
    embeded = discord.Embed(title="Submitted!", description='Thank you '+user, color=0xEE8700)
    embeded.set_image(url="https://images-ext-2.discordapp.net/external/FFFLzhqCY13iJLePq2XaDR-4AU3FzkAEfjS64nMICKo/https/plcooke.com/images/joobertai/goodjoobert%21.png")
    await ctx.send(embed=embeded)
    sendchannel=client.get_channel(729424452479090690)
    await sendchannel.send("\""+str(ctx.message.content).replace("$feedback ","")+"\" from "+str(ctx.message.author.mention))

@client.command()
async def zimbabwe(channel,*,message):
    channel = client.get_channel(735080537319932005)
    await channel.send(message)

@client.command()
async def man(channel,*,message):
    channel = client.get_channel(751076705829126286)
    await channel.send(message)
    
@client.command()
async def the(channel,*,message):
    channel = client.get_channel(703049875373162607)
    await channel.send(message)


@client.command()
async def status(ctx):
    runtime="Joobert AI is currently operational and has been for "
    timeleft=str(time.time()-startuptime)
    timeleft=timeleft[:timeleft.find(".")]
    timeleft=int(timeleft)
    if timeleft>86400:
        days=str(timeleft/86400)
        days=days[:days.find(".")]
        runtime=runtime+days+" days, "
        timeleft=timeleft-(int(days)*86400)
    if timeleft>3600:
        hours=str(timeleft/3600)
        hours=hours[:hours.find(".")]
        runtime=runtime+hours+" hours, "
        timeleft=timeleft-(int(hours)*3600)
    if timeleft>60:
        minutes=str(timeleft/60)
        minutes=minutes[:minutes.find(".")]
        runtime=runtime+minutes+" minutes, "
        timeleft=timeleft-(int(minutes)*60)
    runtime=runtime + str(timeleft) +" seconds"
    await ctx.send(runtime) 

@client.command()
async def dice(ctx,*,message):
    roll = (random.randint(1,6))
    if (roll == 1):
        await ctx.send("You rolled a 1")
    if (roll == 2):
        await ctx.send("You rolled a 2")
    if (roll == 3):
        await ctx.send("You rolled a 3")
    if (roll == 4):
        await ctx.send("You rolled a 4")
    if (roll == 5):
        await ctx.send("You rolled a 5")
    if (roll == 6):
        await ctx.send("You rolled a 6")

@client.command()
async def coin(ctx):
    coin = (random.randint(1,2))
    if (coin == 1):
        await ctx.send("Heads")
    else:
        await ctx.send("Tails")

@client.command()
async def eightball(ctx):
    ballAnswer = random.choice(ballList)
    await ctx.send(ballAnswer)


client.run('INSERT TOKEN')
