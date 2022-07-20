import discord
import re

from discord.ext import commands, tasks
intents = discord.Intents().all()
bot = commands.Bot(command_prefix="er ", intents=intents)

@bot.command()
def c(bot, from, money, to):
  pass

def u(bot):
  pass

def l(bot):
  pass

def help(bot, command=None):
  if command==None:
    pass
  else:
    pass
  
def f(bot, from=None, add=None, remove=None, calculate=None):
  if from==None and add==None and remove==None and calculate==None:
    pass
  elif from!=None and add==None and remove==None and calculate==None:
    pass
  elif from==None and add!=None and remove==None and calculate==None:
    pass
  elif from==None and add==None and remove!=None and calculate==None:
    pass
  elif from==None and add==None and remove==None and calculate!=None:
    pass
  else:
    pass
  
