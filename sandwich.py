import pymongo
import discord
import asyncio
from enum import Enum
import random
from discord.ext import commands
import logging
import string

#do not edit
bot = commands.Bot(command_prefix =';;', pm_help = True)
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
admins = ['162330485714845696', 131182268021604352]
@bot.event
async def on_ready():
    print('Logged in as '+ bot.user.name, "with id "+ bot.user.id, '\n')
    bot.change_presence(game='give me something to do to kill some time', status='dnd')
#Change from here on!

@bot.command(pass_context=True)
async def order(ctx, *, orderdescription: str):
    """Order something!"""
    l = [x for x in sandwiches if x.customer == ctx.message.author.id]
    if len(l) > 0:
        await bot.say('cANT yOU aLREAD hAVE ORDERINO')
        return
    neworder = Sandwich()
    neworder.customer = ctx.message.author.id
    neworder.description = orderdescription
    neworder.server = ctx.message.server.id
    neworder.channel = ctx.message.channel.id
    sandwiches.append(neworder)
    print(len(sandwiches))
    await bot.say('You got it!')
    await bot.send_message(discord.Object(id='351140670255398912'), 'new orderino')


@bot.command(pass_context=True)
async def orderinfo(ctx, orderid: str):
    """Get order info."""
    l = [x for x in sandwiches if x.id == orderid]
    if len(l) > 0:
        order = l[0]
        await bot.say('Order info yo \r\n'+order.id+'\r\n'+order.description+'\r\n'+order.customer+'\r\n'+str(order.status))
    else:
        await bot.say('cant find order bud');


@bot.command(pass_context=True)
async def deliver(ctx, orderid: str):
    """DELIVER"""
    l = [x for x in sandwiches if x.id == orderid]

    if len(l) > 0:
        order = l[0]
        if order.status == Status.Accepted or order.status == Status.ReadyForDelivery:
            chan = bot.get_channel(order.channel)
            user = bot.get_user_info(order.customer)
            inv = await bot.create_invite(chan)
            await bot.send_message(ctx.message.author, str(inv) )
            us = await bot.get_user_info(order.customer)
            await bot.send_message(us, 'hey, '+ctx.message.author.name+' is **DELIVERYING** your order, watch out!')
        else:
            await bot.say('no can do, this order aint ready to deliver');
    else:
        await bot.say('cant find order bud');


@bot.command(pass_context=True)
async def acceptorder(ctx, orderid: str):
    """Accept order."""
    l = [x for x in sandwiches if x.id == orderid]

    if len(l) > 0:
        order = l[0]
        print(order.chef)
        if order.chef == 0:
            if order.status == Status.Waiting:
                await bot.say('roger that! put it in the cooky machine with ;cookymachine <orderid>')
                sandwiches.remove(order)
                order.status = Status.Accepted
                order.chef = ctx.message.author.id
                us = await bot.get_user_info(order.customer)
                await bot.send_message(us, 'hello, '+ctx.message.author.name+' has **acceoted** your order...woo!')
                sandwiches.append(order)
            else:
                await bot.say('i dont know what suspisciscosus stuff you be doing, but this order cant be accepted.')
        else:
            await bot.say('again, no can do. you aint the owner if this
async def game(ctx, *, game : str):
    """Set game."""
    if ctx.message.author.id == "131182268021604352":
        await bot.change_presence(game=discord.Game(name = str(game)))
        await bot.say("done")
    else:
        await bot.say('you dont own me.')

@bot.command(pass_context=True)
async def getallorders(ctx):
    """Gets all orders."""
    orders = ""
    for x in sandwiches:
        orders+="`"+str(x.id)+"`, "
       
    await bot.say(orders)

@bot.command(pass_context=True)
async def shutdown(ctx):
    if ctx.message.author.id in admins:
        await bot.say("Adios")
        bot.logout()
    else:
        await bot.say("error: permission denied")
        print(ctx.message.author, "("+ctx.message.author.id+")", "tried to shutdown the bot!")
 order.')
    else:
        await bot.say('cant find order eh');

@bot.command(pass_context=True)
async def denyorder(ctx, orderid: str):
    """Deny an order."""
    l = [x for x in sandwiches if x.id == orderid]

    if len(l) > 0:
        order = l[0]
        if order.chef == 0:
                await bot.say('roger, deleterationatering')
                us = await bot.get_user_info(order.customer)
                await bot.send_message(us, 'hello, mister '+ctx.message.author.name+' has deleted your order. dont know why...')
                sandwiches.remove(order)
                await bot.say('done.')
        else:
            await bot.say('again, no can do. you aint the owner if this order.')
    else:
        await bot.say('cant find order eh');



@bot.command(pass_context=True)
async def cookymachine(ctx, orderid: str):
    """cook."""
    l = [x for x in sandwiches if x.id == orderid]

    if len(l) > 0:
        order = l[0]
        if order.chef == ctx.message.author.id and order.status == Status.Accepted:
            await bot.say('cookying the sammich')
            sandwiches.remove(order)
            order.status = Status.Cooking
            sandwiches.append(order)
            us = await bot.get_user_info(order.customer)
            await bot.send_message(us, 'SUP, '+ctx.message.author.name+' is TOASTING your order.')
            await asyncio.sleep(30)
            sandwiches.remove(order)
            order.status = Status.ReadyForDelivery
            sandwiches.append(order)
            await bot.say('done cooking '+order.id)
        else:
            await bot.say('either you dont own this order or it isn\'t accepted. i dunno, fix it')
    else:
        await bot.say('cant find order eh');

@bot.command(pass_context=True)
bot.run('no token, sorry')