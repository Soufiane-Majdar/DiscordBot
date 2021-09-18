# Import the required packages
import discord
from discord.ext import commands
from webserver import keep_alive
import os
from bs4 import BeautifulSoup
import requests
import time
client = discord.Client()

@client.event
async def on_ready():
  print("👍 Bot is up now!")



@client.event
async def on_message(message):
  s=0
  if message.content.startswith('$hello'):
    await message.channel.send('👋Hello!')
  
  elif message.content.startswith('$about'):
    embedVar = discord.Embed(title="Bot🤖", description="This bot helps to support on latest technologies", color=0x0099ff)
    await message.channel.send(embed=embedVar)

  elif message.content.startswith('$how are you?'):
    await message.channel.send('Iam super👌. How are your?')

  elif message.content.startswith('$Iam fine.'):
    await message.channel.send('Ok. How may i help you?')

  elif message.content.startswith('achno smaytek'):
    await message.channel.send('smayti Majdar_Learning  Robot!🤖')

  elif message.content.startswith('$How you built?'):
    await message.channel.send('Using python🐍 & discord👨‍🎓')

  elif message.content.startswith('$version'):
    await message.channel.send('Version 1.0.0')
    
  elif message.content.startswith('$bye'):
    await message.channel.send('👋Bye!. See you Soon.')

  elif message.content.startswith('$How to learn python?'):
    await message.channel.send('Refer the github repo - https://github.com/mGalarnyk/Python_Tutorials')

  elif message.content.startswith('l3ez'):
    await message.channel.send('hanya wayli.')

  elif message.content.startswith('7bass'):
    s=1
    await message.channel.send('ok ana an7bass.')

    
  elif 'idea' in message.content:
      if '10 twani' in message.content:
          while (s<1):
                    # 1.Fetch the pages (write the website you wish to scrape within parentheses)
                    result = requests.get("https://thisideadoesnotexist.com/")
                    # 2.Get the page content
                    content = result.text
                    # 3. Create the soup
                    soup = BeautifulSoup(content, "lxml")
                    element = soup.find('h2')
                    await message.channel.send('Idea you might like : \n'+element.text)
                    time.sleep(10)
  """elif 'i want to learn' in message.content:
      if 'html' in message.content:
                    # 1.Fetch the pages (write the website you wish to scrape within parentheses)
                    result = requests.get("https://thisideadoesnotexist.com/")
                    # 2.Get the page content
                    content = result.text
                    # 3. Create the soup
                    soup = BeautifulSoup(content, "lxml")
                    element = soup.find('h2')
                    await message.channel.send(element)
      else:
        await message.channel.send('wahat you you want to learn can you please specifiy ..')"""


  

# Flask Code which will act as server
keep_alive()

# Robot Token Value
TOKEN = 'ODg4NzI1Mzc5ODE1MTg2NDU0.YUW4Ag.vhYNoCmFgTBzT6r7So2wIICwHdk'

client.run(TOKEN)