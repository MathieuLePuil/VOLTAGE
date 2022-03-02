import discord
from discord.ext import commands
import datetime
import asyncio
import random
import json
import re
from discord_slash import cog_ext

class Kick(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@cog_ext.cog_slash(name = "kick", description = "Kick un utilisateur.")
	@commands.has_permissions(kick_members = True)
	async def kick(self, ctx, user : discord.User, *, reason = "Aucune raison n'a été renseignée!"):

		log_channel = self.bot.get_channel(853703546028818443)

		await self.first_kick(user)
		users = await self.get_kick_data()
		date = datetime.datetime.now()

		em = discord.Embed(description = f"**{user}** a été kick! \n \n **Raison:** {reason}", color = 0xFF1700)
		em.set_thumbnail(url = user.avatar_url)

		try:

			if users[str(user.id)]["1er Kick"] == "Aucune":
				users[str(user.id)]["1er Kick"] = reason
				users[str(user.id)]["k-Jour1"] = date.day
				users[str(user.id)]["k-Mois1"] = date.month
				users[str(user.id)]["k-Annee1"] = date.year
				users[str(user.id)]["k-Heure1"] = date.hour
				users[str(user.id)]["k-Minute1"] = date.minute
				await ctx.send(embed = em)
				await log_channel.send(embed = em)
			elif users[str(user.id)]["1er Kick"] != "Aucune" and users[str(user.id)]["2eme Kick"] == "Aucune":
				users[str(user.id)]["2eme Kick"] = reason
				users[str(user.id)]["k-Jour2"] = date.day
				users[str(user.id)]["k-Mois2"] = date.month
				users[str(user.id)]["k-Annee2"] = date.year
				users[str(user.id)]["k-Heure2"] = date.hour
				users[str(user.id)]["k-Minute2"] = date.minute
				await ctx.send(embed = em)
				await log_channel.send(embed = em)
			elif users[str(user.id)]["2eme Kick"] != "Aucune":
				em1 = discord.Embed(description = f"Le joueur {user.name} a déjà reçu 2 kicks.", color = 0xFF1700)
				await ctx.send(embed = em1)

		except KeyError:
			print(f"Il y a une erreur!")

		emkick = discord.Embed(description = f"⛔ Vous avez été kick du **`ScaryShop`** pour ***{reason}*** !", color = 0xFF1700)
		await user.send(embed = emkick)

		await ctx.guild.kick(user, reason = reason)


		with open("kicks.json", "w") as f:
			users = json.dump(users, f, indent = 2)

	async def first_kick(self, user):

	    users = await self.get_kick_data()
	    name = f"{user.name}#{user.discriminator}"

	    if str(user.id) in users:
	        return False
	    else:
	        
	        users[str(user.id)] = {}
	        users[str(user.id)]["user_name"] = name
	        users[str(user.id)]["1er Kick"] = "Aucune"
	        users[str(user.id)]["k-Jour1"] = 0
	        users[str(user.id)]["k-Mois1"] = 0
	        users[str(user.id)]["k-Annee1"] = 0
	        users[str(user.id)]["k-Heure1"] = 0
	        users[str(user.id)]["k-Minute1"] = 0
	        users[str(user.id)]["2eme Kick"] = "Aucune"
	        users[str(user.id)]["k-Jour2"] = 0
	        users[str(user.id)]["k-Mois2"] = 0
	        users[str(user.id)]["k-Annee2"] = 0
	        users[str(user.id)]["k-Heure2"] = 0
	        users[str(user.id)]["k-Minute2"] = 0

	    with open("kicks.json", "w") as f:
	        users = json.dump(users, f, indent = 2)
	    return True

	async def get_kick_data(self):
	    with open("kicks.json", "r") as f:
	        users = json.load(f)

	    return users


def setup(bot):
  	bot.add_cog(Kick(bot))