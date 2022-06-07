import random
import discord
from discord.ext import commands
from discord.utils import get
import playsound
from gtts import gTTS
import os
from discord import File

def speak(text): 
    textas = gTTS(text=text, lang="en", slow=False)
    filename = "sir.mp3"
    textas.save(filename)


client = commands.Bot(command_prefix='?')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('with secrets'))
    print("bot is launched")


@client.event
async def on_message(message):
    if message.author == client.user:
      return

    if message.content == 'xD':
      speak("YOu are noob stop using that word!")
      await message.channel.send(file=File("sir.mp3"))
    else:
      pass
      await client.process_commands(message)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error,commands.CommandNotFound):
        await ctx.send('This Command does not exist!')

@client.command()
async def dm(ctx, user: discord.User = None, *, value = None):
       await user.send(value)
       speak(value)
       await user.send(file=File("sir.mp3"))


@client.command()
async def talk(ctx,*, text):
  speak(text)
  await ctx.send(file=File("sir.mp3"))




@client.command()
async def coinflip(ctx):
    coinflips = ['Heads', 'Tails'] 
    await ctx.send(f'The Coin landed on **{random.choice(coinflips)}**')

@client.command()
async def remove(ctx, amount : int):
				await ctx.channel.purge(limit=amount)
#remove errors
@remove.error
async def remove_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Missing amount of messages to remove!')

@client.command()
async def ping(ctx): 
    ping = f'Your Ping iS{round(client.latency * 1000)}ms'
    speak(ping)
    await ctx.send(file=File("sir.mp3"))
#ping and as
    
@client.command()
async def ask(ctx, * , question):
    responses = ['your mom gay!',
                 'No',
                 'yes',
                 '我有大 JB 想吃吗?',
                 'Noob idc',
                 'No one asked',
                 'I think you should stfu',
                 'yes but no',
                 'no but yes',
                 'do you really think i will reply with yes or no',
                 'the sky is nice',
                 'cao ni ma 闭嘴',
                 '你在狗叫什么',
                 '本座乃虎牙TV第一战神,9国服打野无规则打野创始人,狼队总教练东星耀扬是也。']
 
    await ctx.send(f'**{ctx.message.author}** asked: {question}\nResponse: {random.choice(responses)}')

@ask.error
async def ask_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Missing Arguments to this command')
    

