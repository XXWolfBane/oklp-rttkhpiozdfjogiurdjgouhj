import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    
@bot.command()
async def ping(ctx):
    await ctx.send('Pong! My ping is'.format(round(bot.latency, 1) 
                                             
                                             
@bot.command
async def hug(ctx):
    await ctx.send('*Hugs ' + discord.message.AuthorUserName + '*')

@bot.command
async def greet(ctx):
    await ctx.send("Hello there! :wave:")
    

     
bot.run('NDcxMDY2MjIzNDcyMjc5NTU0.Djfa0A.Z0jGAYYwwAi5UyzsGj1QqDBUBME')

