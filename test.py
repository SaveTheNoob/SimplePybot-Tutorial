import random
import discord
from discord.ext import commands




client = commands.Bot(command_prefix='?')

#This part is when the discord bot is ready it sets the status and the activity of it 
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('with secrets'))
    print("bot is launched")

#the bot will response to a message if it includes xD
@client.event
async def on_message(message):
    if message.author == client.user:
      return

    if message.content == 'xD':
      await message.channel.send("NOpls no")
    else:
      pass
      await client.process_commands(message)

#if the user type a command that doesnt exist it will send message noticing them 
@client.event
async def on_command_error(ctx, error):
    if isinstance(error,commands.CommandNotFound):
        await ctx.send('This Command does not exist or spelling is wrong!')

#dms the user, if user attempt to dm himself it will send message and if it is missing arguments it will send message until requirments are done
@client.command()
async def dm(ctx, user: discord.User = None, *, message = None):
  if user == ctx.message.author:
    await ctx.send("User attempted to dm himself")
  else:
    if user or message == None:
      await ctx.send('Missing Arguments, Make sure to follow format ?dm /userid /message')
    else:
       await user.send(message)


#creates text channel
@client.command()
async def createTextC(ctx, channel_name = None):
  guild = ctx.guild
  if channel_name == None:
    await ctx.send("Please type set a name for the channel")
  else:
    await guild.create_text_channel(channel_name)

#creates voice channel
@client.command()
async def createVoiceC(ctx, channel_name=None):
  guild = ctx.guild
  if channel_name == None:
    await ctx.send("Please type set a name for the channel")
  else:
    await guild.create_voice_channel(channel_name)

#removes all the channels
@client.command()
async def removechall(ctx):
  for ch in ctx.guild.channels:
    await ch.delete()

#COINFLIP!
@client.command()
async def coinflip(ctx):
    coinflips = ['Heads', 'Tails'] 
    await ctx.send(f'The Coin landed on **{random.choice(coinflips)}**')

#remove text message 
@client.command()
async def remove(ctx, amount : int):
				await ctx.channel.purge(limit=amount)
#checks error for remove
@remove.error
async def remove_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Missing amount of messages to remove!')
#PING , checks the ping of the client
@client.command()
async def ping(ctx):
    await ctx.send(f'Ping {round(client.latency * 1000)}ms')

  #Ask a question and the bot will choose random things to say from the reponses
@client.command()
async def ask(ctx, * , question):
    responses = ['your mom gay!',
                 'No',
                 'yes',
                 'HAahahahahaahaahh',
                 'Noob idc',
                 'No one asked',
                 'I think you should stfu',
                 'yes but no',
                 'no but yes',
                 'do you really think i will reply with yes or no',
                 'the sky is nice',
                 'FACKOFF',
                 '你在狗叫什么',
                 '本座乃虎牙TV第一战神,9国服打野无规则打野创始人,狼队总教练东星耀扬是也。']
 
    await ctx.send(f'**{ctx.message.author}** asked: {question}\nResponse: {random.choice(responses)}')
#checks for the error of Ask
@ask.error
async def ask_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Missing Arguments to this command')
    

client.run("Your discord BOT token ")#Discord Bot Token not user token