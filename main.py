import discord
from discord.ext import commands
import json

with open('setting.json',mode='r',encoding='utf8')as jflie:
    jdata = json.load(jflie)#讀取json資料

intents = discord.Intents.all() 
intents.members = True 

bot = commands.Bot(command_prefix="+", intents=intents) # "Import" the intents

@bot.event
async def on_ready():
    print(">>Bot is online<<") #改寫定義顯示在線上


@bot.event
async def on_member_join(member):
    channel=bot.get_channel(int(jdata['Both_channel']))#字串變整數
    await channel.send(f'{member}fall in love!')#成員加入 await:if your code is the coroutine than you must use it.

@bot.event
async def on_member_remove(member):
     channel=bot.get_channel(int(jdata['Both_channel']))
     await channel.send(f'{member}break up!')#成員離開

@bot.command()
async def breakup(ctx):
    await ctx.send('竜神の剣を喰らえ')#回覆

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}ms')#顯示當前ping值





bot.run(jdata['TOKEN']) #連結自己的bot  
