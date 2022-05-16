import discord
import pytz
from discord.ext import commands
import json
import asyncio
import datetime
import requests
import os
from dotenv.main import load_dotenv

load_dotenv()
intents = discord.Intents.default()
client = commands.Bot(command_prefix=';', intents = intents)

def do_mongo_stuff():
    from pymongo import MongoClient
    cluster = MongoClient(os.getenv("MONGOURL"))
    db = cluster['supplement_database']
    collection = db['supplement_collection']
    x = collection.find_one({"_id":"data"})
    global data
    data = x['value']
#do_mongo_stuff()


@client.event
async def on_ready():
    print("Bot is online")

@client.command()
async def hello(ctx):
    embed = discord.Embed(title = ctx.author.name,description ="Hello",color=0xff7d00)
    await ctx.send(embed=embed)


@client.command()
async def setjson(ctx):
    with open('testjson.json', 'w') as f:
        data={'1':[1,2,3,4],'2':[11,12,13,14]}
        json.dump(data, f, indent=2)


@client.command()
async def incjson(ctx):
    with open('testjson.json', 'r') as f:
        data = json.load(f)

    data['1'][0] += 1
    with open('testjson.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    await ctx.send(data)


client.run(os.getenv("TOKEN2"))