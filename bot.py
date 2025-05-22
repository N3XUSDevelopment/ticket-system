# thatoneracer_ on discord made this.
# Property of NEXUS Development
# We arent using cogs due to the small size of this code, it is not needed

import discord
from discord.ext import commands
from discord import app_commands
import json
import os 

# handlers
with open(os.path.join(os.path.dirname(__file__), "config.json")) as f:
    config = json.load(f)
    token = config['token']
    ticketcategoryid = config['ticket-category-id']
    ticketchannelid = config['ticket-selection-channel-id']
    supportid = config['support-role-id']

async def ticket_selection_message():
    channel = bot.get_channel(ticketchannelid)
    for message in channel.history(limit=200):
        if message.author.id == bot.user.id: message.delete()
    
    embed = discord.Embed(title=f"**{channel.guild.name} Ticket Selection**", description="Select your tickets here! Please make sure its the respective ticket for your situation.")
    # embed = discord.Embed(title=f"**Ticket Selection**", description="Select your tickets here! Please make sure its the respective ticket for your situation.")
    general = discord.ui.Button(label="Open a General Support Ticket!", style=discord.ButtonStyle.green)
    report = discord.ui.Button(label="Open a Report Ticket!", style=discord.ButtonStyle.red)
    store = discord.ui.Button(label="Open a Store Support Ticket!", style=discord.ButtonStyle.green)   
    async def generalc(i: discord.Interaction):
        if  

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event()
async def on_ready():
    print(f"Logged into {bot.user.name} ({bot.user.id})")

bot.run(token)