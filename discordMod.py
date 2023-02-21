import discord
#import os
from watchpubs import get_watchpubs_link, get_movie_link

client = discord.Client(intents=discord.Intents.all())
#TOKEN = os.environ['TOKEN']

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith("$hello"):
    await message.channel.send('Hello!')
  
  elif message.content.startswith("$help"):
    await message.channel.send('Help!')

  elif message.content.startswith("$moviealone"):
    await message.channel.send('Your video link will be sent in one minute')
    movieName = message.content.split("$moviealone ")[1].strip()
    await message.channel.send(get_movie_link(movieName))

  elif message.content.startswith("$movie"):
    await message.channel.send('Your WatchPubs link will be sent in one minute')
    movieName = message.content.split("$movie ")[1].strip()
    await message.channel.send(get_watchpubs_link(movieName))

client.run('MTA3NzM5MzU4NDcwMzE1NjI5NA.GyOs8L.lFH3S3qnkx1qP8DWBZYT3AzJqAgjh2iPErmHr8')