import discord
from discord.ext import commands
import json
from discord_slash import SlashCommand

intents = discord.Intents.default()
intents.typing = True
intents.presences = True
intents.members = True
intents.reactions = True


# py desktop\Bots_Discord\Voltage\main.py


async def get_prefix(message):
    with open("/home/mmi21b12/DISCORD/VOLTAGE/prefixes.json", "r") as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]


bot = commands.Bot(command_prefix=get_prefix, intents=intents)
bot.remove_command("help")
bot.remove_command("clear")
slash = SlashCommand(bot, sync_commands=True)

extensions = ['clear', 'prefix', 'mute', 'warn', 'ban', 'reset', 'sanction', 'help', 'on_command_error', 'kick',
              'latence', 'prison']


@bot.event
async def on_ready():
    print("Le Bot Voltage est PRET!")


@slash.slash()
@commands.has_permissions(ban_members=True)
async def load(ctx, extension):
    try:
        bot.load_extension(extension)
        await ctx.send('Loaded **{}**'.format(extension))
    except Exception as error:
        await ctx.send('**{}** cannot be loaded. [{}]'.format(extension, error))


@slash.slash()
@commands.has_permissions(ban_members=True)
async def unload(ctx, extension):
    try:
        bot.unload_extension(extension)
        await ctx.send('Unloaded **{}**'.format(extension))
    except Exception as error:
        await ctx.send('**{}** cannot be unloaded. [{}]'.format(extension, error))


if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as error:
            print('**{}** cannot be loaded. [{}]'.format(extension, error))


@slash.slash()
@commands.has_permissions(ban_members=True)
async def reload(ctx, extension):
    if extension:
        try:
            bot.reload_extension(extension)
            await ctx.send('Reloaded **{}**'.format(extension))
        except:
            bot.load_extension(extension)
            await ctx.send('Loaded **{}**'.format(extension))


bot.run("ODUxMDc4MTc3MzM3MjQ1NzY3.YLzCUQ.Msm7HyLHihmQ_JyQFo28psaYkco")
