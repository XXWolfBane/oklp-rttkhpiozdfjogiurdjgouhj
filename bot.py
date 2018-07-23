import discord
import discord.ext import commands

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    
@bot.command()
async def createticket(pass_contex=TRUE):
    r=raident.random
    await bot.send_message(ctx.message.channel, "You support number is" + str(r) + "please wait for staff to see this."
    
@bot.command()
async def staff.claim(userName: discord.User, ticketNumber: int(a), ctx)
     await bot.send_message(ctx.message.channel, userName + "Has claimed call number" + ticketNumber)
     
bot.run('NDcxMDY2MjIzNDcyMjc5NTU0.Djfa0A.Z0jGAYYwwAi5UyzsGj1QqDBUBME')

