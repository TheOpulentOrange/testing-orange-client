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
async def test(ctx):
    for member in ctx.guild.members:
        print(member)

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
    
    print(data)


dank_item_valuation = {
 'cash': [1, ':coin: Cash'],
 'grinder': [1, '💸 Grinder'],
 'heist': [1, '🏦 Heist'],
 'events':[1,'🎁 Events'],
    
 'adv': [110000, 'Adventure tickets'],
 'alc': [6500, 'Alcohol'],
 'alien': [1100000, 'Alien sample'],
 'ammo': [2000000, 'Ammo'],
 'ant': [10000, 'Ant'],
 'anti': [400000, 'Anti-rob pack'],
 'apple': [4500, 'Apple'],
 'apron': [1000000, "Bunny's apron"],
 'armpit': [3200000, 'Armpit hair'],
 'baby': [1000000, 'Baby'],
 'badge': [1100000, 'Police badge'],
 'bait': [1500000, 'Fishing bait'],
 'ban': [750000, 'Ban hammer'],
 'beaker': [3800000, 'Beaker of sus fluid'],     
 'bean': [170000, 'Bean'],
 'beard': [18000000, "Melmsie's beard"],
 'berries': [25000000, 'Berries and cream'],     
 'binary': [3000000, 'Binary'],
 'blob': [5550000000, 'Blob'],
 'blue': [3696, 'Blue phallic object'],
 'boar': [17500, 'Boar'],
 'bolt': [137000000, 'Bolt cutters'],
 'bomb': [18000, 'Coin bomb'],
 'bread': [7000, 'Fresh bread'],
 'camera': [1600000, 'Camera'],
 'candy': [13000, 'Candy'],
 'cane': [30000, 'Candy cane'],
 'card': [1250000000, "Enchanted Badosz's card"],
 'cell': [500, 'Cell phone'],
 'cheese': [25000, 'Shredded Cheese'],
 'chill': [12000, 'Chill pill'],
 'chocolate': [75000000, 'Boxed chocolates'],    
 'christmas': [10000000, 'Christmas tree'],      
 'common': [8000, 'Common fish'],
 'cookie': [4000, 'Cookie'],
 'corncob': [210000, 'Corncob'],
 'corndog': [230000, 'Corndog'],
 'credit': [150000000, 'Credit card'],
 'crown': [190000000, 'Pepe Crown'],
 'cursed': [76000000, 'Cursed Pepe'],
 'dank': [1100000, 'Dank box'],
 'deer': [65000, 'Deer'],
 'diaper': [900000, 'Used diaper'],
 'dragon': [200000, 'Dragon'],
 'duck': [9000, 'Duck'],
 'ecto': [1000000, 'Ectoplasm'],
 'energy': [2200000, 'Energy drink'],
 'exotic': [20000, 'Exotic fish'],
 'fake': [6000, 'Fake id'],
 'fart': [80000000, 'Empowered fart bottle'],
 'fartina': [14000000, 'Fart in a bottle'],
 'flower': [3000000, "Aetheryx' Flower"],
 'fools': [100000, "Fool's notif"],
 'fossil': [750000, 'Fossil'],
 'freeze': [5000000, 'Streak freeze'],
 'friends': [200000, "Friend's gift"],
 'garbage': [4000, 'Garbage'],
 'gec': [8000000, 'Prestige coin'],
 'giftbox': [400000, 'Gift box'],
 'god': [27000000, 'God box'],
 'gold': [860000, 'Golden corndog'],
 'goldenp': [100000, 'Golden phallic object'],
 'goldenphallic': [100000, 'Golden phallic object'],
 'green': [3075000, 'Green screen'],
 'grind': [600000, 'Grind pack'],
 'grinder': [1, 'Grinder'],
 'headphones': [4200000, 'Headphones'],
 'heist': [1, 'Heist'],
 'hole': [125000, 'Black hole'],
 'ily': [140000, 'Daily box'],
 'jacky': [3000000, "Jack o' lanty"],
 'jar': [500000, 'Jar of Singularity'],
 'jelly': [40000, 'Jelly fish'],
 'junk': [9500, 'Junk'],
 'karen': [325000000, 'Literally Karen'],
 'keyboard': [46000, 'Keyboard'],
 'knote': [110000, 'Bank note'],
 'kraken': [415000, 'Kraken'],
 'ladybug': [12000, 'Ladybug'],
 'laptop': [16000, 'Laptop'],
 'law': [4000000, 'Law degree'],
 'leg': [200000, 'Legendary fish'],
 'letter': [9000000, 'The letter'],
 'life': [39000, 'Life saver'],
 'light': [2700000, 'Ring light'],
 'like': [1000000, 'Like button'],
 'lock': [4500, 'Padlock'],
 'mask': [2000000, 'Robbers mask'],
 'meme': [400000, 'Meme box'],
 'mete': [300000, 'Meteorite'],
 'mic': [3100000, 'Microphone'],
 'mine': [6000, 'Landmine'],
 'mouse': [45000, 'Mouse'],
 'mp3': [21000000, 'Bean MP3 player'],
 'multi': [900000, 'Multi coloured phallic object'],
 'new': [250000, 'New player pack'],
 'normie': [130000, 'Normie box'],
 'note': [2000000, 'Musical note'],
 'odd': [1300000000, 'Odd eye'],
 'orange': [20000, 'Orange phallic object'],
 'ornament': [42000, 'Ornament'],
 'oszcard': [5000000, "Badosz's card"],
 'paper': [225000000, 'Toilet paper'],
 'pat': [14000000, 'Patreon box'],
 'patpack': [14000000, 'Patreon pack'],
 'pepec': [275000, 'Pepe Coin'],
 'pepem': [5000000, 'Pepe Medal'],
 'pepes': [600000000, 'Pepe sus'],
 'pepestat': [250000, 'Pepe Statue'],
 'pepet': [38000000, 'Pepe Trophy'],
 'pet': [5000000, 'Pet collar'],
 'pills': [5500000, 'Meme pills'],
 'pink': [25, 'Pink phallic object'],
 'pizza': [99000, 'Pizza slice'],
 'plane': [650000, "Blue's plane"],
 'plus': [3300000, 'A plus'],
 'pole': [10000, 'Fishing pole'],
 'poster': [4000000, 'Motivational'],
 'potato': [150000, 'Potato'],
 'pres': [5500000, 'Prestige pack'],
 'purple': [15000, 'Purple phallic object'],
 'rabbit': [7500, 'Rabbit'],
 'rare': [25000, 'Rare Pepe'],
 'raref': [11000, 'Rare fish'],
 'rev': [10000000, 'Reversal card'],
 'ribbon': [400000000, 'Pepe ribbon'],
 'rifle': [10000, 'Hunting rifle'],
 'ring': [350000, 'Engagement ring'],
 'sand': [3000, 'Box of sand'],
 'sbag': [9500000, "Santa's bag"],
 'scepter': [10000000, 'Royal scepter'],
 'school': [12000000, 'School urinal'],
 'seaweed': [1000, 'Seaweed'],
 'shat': [34000, "Santa's hat"],
 'shoe': [28000, 'Lucky horseshoe'],
 'shooting': [1100000, 'Shooting star'],
 'shop': [2500000, 'Shop coupon'],
 'shovel': [10000, 'Shovel'],
 'shovels': [10000, 'Shovel'],
 'skull': [40000000, 'Sugar skull'],
 'skunk': [6000, 'Skunk'],
 'snow': [20000, 'Snowball'],
 'snowflake': [45000, 'Snowflake'],
 'sound': [3100000, 'Sound card'],
 'spider': [300000, 'Spider'],
 'spinner': [22000, 'Fidget spinner'],
 'stack': [7000000, 'Stack of cash'],
 'star': [2800000, 'Star fragment'],
 'stickbug': [14000, 'Stickbug'],
 'stocking': [60000000, 'Holiday stocking'],
 'stonk': [6600000, 'Stonk machine'],
 'taco': [2000000, 'Crunchy taco'],
 'tape': [425000, 'Duct tape'],
 'ticket': [30000000, 'Winning lotto'],
 'tide': [20000, 'Tidepod'],
 'tip': [3000000, 'Tip jar'],
 'toe': [50000, 'Cupids big toe'],
 'trash': [40000, 'Trash'],
 'tree': [140000, 'Literally a tree'],
 'vaccine': [5000000, 'Vaccine'],
 'wedding': [1500000, 'Wedding gift'],
 'whisky': [2000000, 'Bottle of whisky'],
 'wishlist': [32000, 'Robbers Wishlist'],
 'worm': [4000, 'Worm'],
 'yeng': [8500000, 'Yeng gang']}

client.run(os.getenv("TOKEN2"))