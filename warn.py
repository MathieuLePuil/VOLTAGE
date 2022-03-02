import discord
from discord.ext import commands
import datetime
import asyncio
import random
import json
import re
from discord_slash import cog_ext

class Warn(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@cog_ext.cog_slash(name = "warn", description = "Avertis un utilisateur.")
	@commands.has_permissions(kick_members = True)
	async def warn(self, ctx, user : discord.User, *, reason):

		log_channel = self.bot.get_channel(853703546028818443)

		await self.first_warn(user, ctx.guild.id)
		users = await self.get_warn_data()
		date = datetime.datetime.now()

		em = discord.Embed(description = f"**{user}** a été warn! \n \n **Raison:** {reason}", color = 0xFF6C00)
		em.set_thumbnail(url = user.avatar_url)

		try:

			if users[str(user.id)]["1er Warn"] == "Aucune":
				users[str(user.id)]["1er Warn"] = reason
				users[str(user.id)]["w-Jour1"] = date.day
				users[str(user.id)]["w-Mois1"] = date.month
				users[str(user.id)]["w-Annee1"] = date.year
				users[str(user.id)]["w-Heure1"] = date.hour
				users[str(user.id)]["w-Minute1"] = date.minute
				await ctx.send(embed = em)
				await log_channel.send(embed = em)
			elif users[str(user.id)]["1er Warn"] != "Aucune" and users[str(user.id)]["2eme Warn"] == "Aucune":
				users[str(user.id)]["2eme Warn"] = reason
				users[str(user.id)]["w-Jour2"] = date.day
				users[str(user.id)]["w-Mois2"] = date.month
				users[str(user.id)]["w-Annee2"] = date.year
				users[str(user.id)]["w-Heure2"] = date.hour
				users[str(user.id)]["w-Minute2"] = date.minute
				await ctx.send(embed = em)
				await log_channel.send(embed = em)
			elif users[str(user.id)]["2eme Warn"] != "Aucune":
				em1 = discord.Embed(description = f"Le joueur {user.name} a déjà reçu 2 warns.", color = 0xFF6C00)
				await ctx.send(embed = em1)

		except KeyError:
			print(f"Il y a une erreur!")

		with open("warns.json", "w") as f:
			users = json.dump(users, f, indent = 2)


	@commands.Cog.listener()
	async def on_guild_join(self, guild):
	    with open("warns.json", "r") as f:
	        users = json.load(f)

	    users[str(guild.id)] = {}

	    with open("warns.json", "w") as f:
	        json.dump(users, f, indent = 2)

	async def first_warn(self, user, guild):

	    users = await self.get_warn_data()
	    name = f"{user.name}#{user.discriminator}"

	    if str(user.id) in users:
	        return False
	    else:

	        users[str(user.id)] = {}
	        users[str(user.id)]["user_name"] = name
	        users[str(user.id)]["1er Warn"] = "Aucune"
	        users[str(user.id)]["w-Jour1"] = 0
	        users[str(user.id)]["w-Mois1"] = 0
	        users[str(user.id)]["w-Annee1"] = 0
	        users[str(user.id)]["w-Heure1"] = 0
	        users[str(user.id)]["w-Minute1"] = 0
	        users[str(user.id)]["2eme Warn"] = "Aucune"
	        users[str(user.id)]["w-Jour2"] = 0
	        users[str(user.id)]["w-Mois2"] = 0
	        users[str(user.id)]["w-Annee2"] = 0
	        users[str(user.id)]["w-Heure2"] = 0
	        users[str(user.id)]["w-Minute2"] = 0

	    with open("warns.json", "w") as f:
	        users = json.dump(users, f, indent = 2)
	    return True

	async def get_warn_data(self):
	    with open("warns.json", "r") as f:
	        users = json.load(f)

	    return users


def setup(bot):
  	bot.add_cog(Warn(bot))