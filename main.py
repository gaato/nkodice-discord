import random

import discord
import asyncio

from config import DISCORD_TOKEN

client = discord.Client()


@client.event
async def on_ready():
    print('It\'s activated')


async def nkodice(message: discord.Message):

    rolls = random.choices(('う', 'ま', 'ち', 'ん', 'こ', 'お'), k=5)
    roles = []

    if rolls.count('お') >= 1 and rolls.count('ち') >= 2 and rolls.count('ん') >= 2:
        roles.append('OCHINCHIN')
    elif rolls.count('ち') >= 2 and rolls.count('ん') >= 2:
        roles.append('CHINCHIN')

    if rolls.count('お') >= 1 and rolls.count('ま') >= 1 and rolls.count('ん') >= 1 and rolls.count('こ'):
        roles.append('OMANKO')
    elif rolls.count('ま') >= 1 and rolls.count('ん') >= 1 and rolls.count('こ'):
        roles.append('MANKO')

    if rolls.count('ち') >= 1 and rolls.count('ん') and rolls.count('こ'):
        roles.append('CHINKO')

    if rolls.count('う') >= 1 and rolls.count('ん') >= 1 and rolls.count('ち'):
        roles.append('UNCHI')

    if rolls.count('う') >= 1 and rolls.count('ん') >= 1 and rolls.count('こ'):
        roles.append('UNKO')
    
    for r in rolls:
        await message.channel.send(r)
        await asyncio.sleep(1.0)
    
    for r in roles:
        await message.channel.send('***' + r + '***')
        await asyncio.sleep(1.0)


@client.event
async def on_message(message: discord.Message):

    if message.author.bot:
        return
    
    if message.content == '!nkodice':
        await nkodice(message)

client.run(DISCORD_TOKEN)
