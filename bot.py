import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    

     
bot.run('NDcxMDY2MjIzNDcyMjc5NTU0.Djfa0A.Z0jGAYYwwAi5UyzsGj1QqDBUBME')

