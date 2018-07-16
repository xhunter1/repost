import discord
from discord.ext import commands
import asyncio
import time

client=discord.Client()

repostfrom="468066868117372949"
repost2="468111720565702668"

@client.event
async def on_ready():
	global role_list
	await client.change_presence(game=discord.Game(name="reposting..."))
	print("MGUI reposter by Felix loaded!")
	print(client.user.name)
	print(client.user.id)

@client.event
async def on_message(message):
	if message.channel.name==str(client.get_channel(repostfrom)):
		try:
			embed = discord.Embed(title=message.embeds[0]['title'], description=message.embeds[0]['description'], color=message.embeds[0]['color'])
			embed.add_field(name=message.embeds[0]['fields'][0]['name'], value=message.embeds[0]['fields'][0]['value'], inline=message.embeds[0]['fields'][0]['inline'])
			embed.add_field(name=message.embeds[0]['fields'][1]['name'], value=message.embeds[0]['fields'][1]['value'], inline=message.embeds[0]['fields'][1]['inline'])
			embed.add_field(name=message.embeds[0]['fields'][2]['name'], value=message.embeds[0]['fields'][2]['value'], inline=message.embeds[0]['fields'][2]['inline'])
			embed.add_field(name=message.embeds[0]['fields'][3]['name'], value=message.embeds[0]['fields'][3]['value'], inline=message.embeds[0]['fields'][3]['inline'])
			embed.add_field(name=message.embeds[0]['fields'][4]['name'], value=message.embeds[0]['fields'][4]['value'], inline=message.embeds[0]['fields'][4]['inline'])
			embed.add_field(name=message.embeds[0]['fields'][5]['name'], value=message.embeds[0]['fields'][5]['value'], inline=message.embeds[0]['fields'][5]['inline'])
			embed.set_footer(text=message.embeds[0]['footer']['text']+" - cloned by Felix", icon_url=message.embeds[0]['footer']['icon_url'])
			embed.set_thumbnail(url=message.embeds[0]['thumbnail']['url'])
			await client.send_message(client.get_channel(repost2), embed=embed) #REPOST
			print("Reposted! "+time.asctime( time.localtime(time.time())))
		except:
			print("Error! "+time.asctime( time.localtime(time.time())))

client.run("NDY4MTIwMjc4MzcxNzk0OTQ0.Di0i9A.1lWJfOs3paw22vtDmfjMuKeibuM")
