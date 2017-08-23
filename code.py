##NOTE: NEV THIS IS A BURNING MESS AND I'VE BEEN WORKING ON IT FOR HALF AN HOUR
#lol idk how this is gonna go

import logging, discord, datetime, json, sys
from discord.ext import commands
import conf

token = conf.token
#DEBUG = i want to hear the sound of the air moving as a pin drops
#INFO = i want to hear a pin drop
#WARNING = i want to know if something goes wrong
#CRITICAL = do not warn me unless something is on fire


loglevel = logging.DEBUG

bot = commands.Bot(command_prefix='!', description='hi', pm_help=True)

logger = logging.getLogger()
logger.setLevel(logging.INFO)

stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.INFO)
# set a formatter or something here
logger.addHandler(stdout_handler)

@bot.event
async def on_ready():
    bot.start_time = datetime.datetime.now()
    print('Bot started at ', bot.start_time)
    print("Logged in as {} with ID {}".format(bot.user.name, bot.user.id))
    users = sum(1 for user in bot.get_all_members())
    channels = sum(1 for channel in bot.get_all_channels())
    print("Serving {} users in {} channels on {} guilds".format(users, channels, len(bot.servers)))
    game = discord.Game(name='dear god')
    await bot.change_presence(status=discord.Status.idle, game=game)


@bot.command(pass_context=True)
async def source(ctx):
    await bot.reply("it worked")

@bot.event
async def on_server_join(guild):
    logging.info('GUILD_CREATE: {0.name} <{0.id}>'.format(guild))

@bot.event
async def on_server_remove(guild):
    logging.info('GUILD_REMOVE: {0.name} (id {0.id})'.format(guild))

@bot.command(pass_context=True)
async def shutdown(ctx):
    await bot.reply("I'm shutting down now.")
    game = discord.Game(name='Shutting down...')
    await bot.change_presence(status=discord.Status.dnd)
    await bot.logout()



bot.run(token)
