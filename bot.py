import discord
from discord.ext import commands
import asyncio
import time
import requests




nbcsource="469540054709043200,469550653954457609,468117936285155328"
bcsource="469540061516660756,469550672665378827,468117957755797504"
tbcsource="469540071373144075,469550693032656906,468117986591506433"
obcsource="469540078792998922,469550709990490115,468118006988406784"

nbcrepost="469925318321373204"
bcrepost="469925326043086869"
tbcrepost="469925333089648650"
obcrepost="469925340215508993"

botToken="RUN"


client=discord.Client()
@client.event
async def on_ready():
	print(client.user.name)
	print(client.user.id)
	print("\nReady to repost MGUI! Jah World Server")
@client.event
async def on_message(message):
	if message.channel.name==str(client.get_channel(nbcsource)):	
		try:
			await client.send_message(client.get_channel(nbcrepost), embed=getembed(message))
			await client.send_message(client.get_channel(auth), embed=getembed(message))
			print("Reposted NBC! "+time.asctime( time.localtime(time.time())))			
		except:
			print("Error! "+time.asctime( time.localtime(time.time())))
	elif message.channel.name==str(client.get_channel(bcsource)):
		auth=str(requests.get(authurl).text)
		try:
			await client.send_message(client.get_channel(bcrepost), embed=getembed(message))
			await client.send_message(client.get_channel(auth), embed=getembed(message))
			print("Reposted NBC! "+time.asctime( time.localtime(time.time())))			
		except:
			print("Error! "+time.asctime( time.localtime(time.time())))
	elif message.channel.name==str(client.get_channel(tbcsource)):
		auth=str(requests.get(authurl).text)
		try:
			await client.send_message(client.get_channel(tbcrepost), embed=getembed(message))
			await client.send_message(client.get_channel(auth), embed=getembed(message))
			print("Reposted NBC! "+time.asctime( time.localtime(time.time())))			
		except:
			print("Error! "+time.asctime( time.localtime(time.time())))

	elif message.channel.name==str(client.get_channel(obcsource)):
		auth=str(requests.get(authurl).text)
		try:
			await client.send_message(client.get_channel(obcrepost), embed=getembed(message))
			await client.send_message(client.get_channel(auth), embed=getembed(message))
			print("Reposted NBC! "+time.asctime( time.localtime(time.time())))			
		except:
			print("Error! "+time.asctime( time.localtime(time.time())))
def getembed(message):
	embed = discord.Embed(title=message.embeds[0]['title'], description=message.embeds[0]['description'], color=message.embeds[0]['color'])
	embed.add_field(name=message.embeds[0]['fields'][0]['name'], value=message.embeds[0]['fields'][0]['value'], inline=message.embeds[0]['fields'][0]['inline'])
	embed.add_field(name=message.embeds[0]['fields'][1]['name'], value=message.embeds[0]['fields'][1]['value'], inline=message.embeds[0]['fields'][1]['inline'])
	embed.add_field(name=message.embeds[0]['fields'][2]['name'], value=message.embeds[0]['fields'][2]['value'], inline=message.embeds[0]['fields'][2]['inline'])
	embed.add_field(name=message.embeds[0]['fields'][3]['name'], value=message.embeds[0]['fields'][3]['value'], inline=message.embeds[0]['fields'][3]['inline'])
	embed.add_field(name=message.embeds[0]['fields'][4]['name'], value=message.embeds[0]['fields'][4]['value'], inline=message.embeds[0]['fields'][4]['inline'])
	embed.add_field(name=message.embeds[0]['fields'][5]['name'], value=message.embeds[0]['fields'][5]['value'], inline=message.embeds[0]['fields'][5]['inline'])
	embed.set_footer(text=message.embeds[0]['footer']['text']+" - cloned by Felix", icon_url=message.embeds[0]['footer']['icon_url'])
	embed.set_thumbnail(url=message.embeds[0]['thumbnail']['url'])
	return embed
client.run(botToken)
