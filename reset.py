import discord
from discord.ext import commands
import datetime
import asyncio
import random
import json
import re
from discord_slash import cog_ext



class Reset(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@cog_ext.cog_slash(name = "reset", description = "Remet à zero les sanctions d'un utilisateur.")
	@commands.has_permissions(kick_members = True)
	async def reset(self, ctx, sanction_type, user : discord.User):
		em1 = discord.Embed(description = f"Les warns de {user} ont été reset!", color = 0xFF6C00)
		em2 = discord.Embed(description = f"Les mutes de {user} ont été reset!", color = 0xFF6C00)
		em3 = discord.Embed(description = f"Les kicks de {user} ont été reset!", color = 0xFF6C00)
		em4 = discord.Embed(description = f"Les peines de prison de {user} ont été reset!", color = 0xFF6C00)

		log_channel = self.bot.get_channel(853703546028818443)
		
		if sanction_type == "warn":
			await self.first_warn(user)
			users = await self.get_warn_data()

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

			await ctx.send(embed = em1)
			await log_channel.send(embed = em1)

		elif sanction_type == "mute":
			await self.first_mute(user)
			users = await self.get_mute_data()

			users[str(user.id)]["1er Mute"] = "Aucune"
			users[str(user.id)]["m-Jour1"] = 0
			users[str(user.id)]["m-Mois1"] = 0
			users[str(user.id)]["m-Annee1"] = 0
			users[str(user.id)]["m-Heure1"] = 0
			users[str(user.id)]["m-Minute1"] = 0
			users[str(user.id)]["m-Duree1"] = None
			users[str(user.id)]["2eme Mute"] = "Aucune"
			users[str(user.id)]["m-Jour2"] = 0
			users[str(user.id)]["m-Mois2"] = 0
			users[str(user.id)]["m-Annee2"] = 0
			users[str(user.id)]["m-Heure2"] = 0
			users[str(user.id)]["m-Minute2"] = 0
			users[str(user.id)]["m-Duree2"] = None

			with open("mutes.json", "w") as f:
				users = json.dump(users, f, indent = 2)

			await ctx.send(embed = em2)
			await log_channel.send(embed = em2)
			

		elif sanction_type == "kick":
			await self.first_kick(user)
			users = await self.get_kick_data()

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

			await ctx.send(embed = em3)
			await log_channel.send(embed = em3)
			

		elif sanction_type == "prison":
			await self.first_prison(user)
			users = await self.get_prison_data()

			users[str(user.id)]["1ere Prison"] = "Aucune"
			users[str(user.id)]["p-Jour1"] = 0
			users[str(user.id)]["p-Mois1"] = 0
			users[str(user.id)]["p-Annee1"] = 0
			users[str(user.id)]["p-Heure1"] = 0
			users[str(user.id)]["p-Minute1"] = 0
			users[str(user.id)]["p-Duree1"] = None
			users[str(user.id)]["2eme Prison"] = "Aucune"
			users[str(user.id)]["p-Jour2"] = 0
			users[str(user.id)]["p-Mois2"] = 0
			users[str(user.id)]["p-Annee2"] = 0
			users[str(user.id)]["p-Heure2"] = 0
			users[str(user.id)]["p-Minute2"] = 0
			users[str(user.id)]["p-Duree2"] = None

			with open("prisons.json", "w") as f:
				users = json.dump(users, f, indent = 2)

			await ctx.send(embed = em4)
			await log_channel.send(embed = em4)
			

		else:
			em = discord.Embed(description = f"**{sanction_type}** n'exite pas. Merci d'entrer `warn` | `mute` | `prison`| `kick`.", color = 0xFF6C00)
			await ctx.send(embed = em)


	

	async def get_warn_data(self):
	    with open("warns.json", "r") as f:
	        users = json.load(f)

	    return users

	async def get_mute_data(self):
	    with open("mutes.json", "r") as f:
	        users = json.load(f)

	    return users

	async def get_kick_data(self):
	    with open("kicks.json", "r") as f:
	        users = json.load(f)

	    return users

	async def get_prison_data(self):
	    with open("prisons.json", "r") as f:
	        users = json.load(f)

	    return users

	async def get_ban_data(self):
	    with open("bans.json", "r") as f:
	        users = json.load(f)

	    return users

	async def first_warn(self, user):

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


	async def first_mute(self, user):

	    users = await self.get_mute_data()
	    name = f"{user.name}#{user.discriminator}"

	    if str(user.id) in users:
	        return False
	    else:
	        
	        users[str(user.id)] = {}
	        users[str(user.id)]["user_name"] = name
	        users[str(user.id)]["1er Mute"] = "Aucune"
	        users[str(user.id)]["m-Jour1"] = 0
	        users[str(user.id)]["m-Mois1"] = 0
	        users[str(user.id)]["m-Annee1"] = 0
	        users[str(user.id)]["m-Heure1"] = 0
	        users[str(user.id)]["m-Minute1"] = 0
	        users[str(user.id)]["m-Duree1"] = None
	        users[str(user.id)]["2eme Mute"] = "Aucune"
	        users[str(user.id)]["m-Jour2"] = 0
	        users[str(user.id)]["m-Mois2"] = 0
	        users[str(user.id)]["m-Annee2"] = 0
	        users[str(user.id)]["m-Heure2"] = 0
	        users[str(user.id)]["m-Minute2"] = 0
	        users[str(user.id)]["m-Duree2"] = None

	    with open("mutes.json", "w") as f:
	        users = json.dump(users, f, indent = 2)
	    return True


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

	async def first_prison(self, user):

	    users = await self.get_prison_data()
	    name = f"{user.name}#{user.discriminator}"

	    if str(user.id) in users:
	        return False
	    else:
	        
	        users[str(user.id)] = {}
	        users[str(user.id)]["user_name"] = name
	        users[str(user.id)] = {}
	        users[str(user.id)]["1ere Prison"] = "Aucune"
	        users[str(user.id)]["p-Jour1"] = 0
	        users[str(user.id)]["p-Mois1"] = 0
	        users[str(user.id)]["p-Annee1"] = 0
	        users[str(user.id)]["p-Heure1"] = 0
	        users[str(user.id)]["p-Minute1"] = 0
	        users[str(user.id)]["p-Duree1"] = None
	        users[str(user.id)]["2eme Prison"] = "Aucune"
	        users[str(user.id)]["p-Jour2"] = 0
	        users[str(user.id)]["p-Mois2"] = 0
	        users[str(user.id)]["p-Annee2"] = 0
	        users[str(user.id)]["p-Heure2"] = 0
	        users[str(user.id)]["p-Minute2"] = 0
	        users[str(user.id)]["p-Duree2"] = None

	    with open("prisons.json", "w") as f:
	        users = json.dump(users, f, indent = 2)
	    return True


	async def first_ban(self, user):

	    users = await self.get_ban_data()
	    name = f"{user.name}#{user.discriminator}"

	    if str(user.id) in users:
	        return False
	    else:
	        
	        users[str(user.id)] = {}
	        users[str(user.id)]["user_name"] = name
	        users[str(user.id)]["1er Ban"] = "Aucune"
	        users[str(user.id)]["b-Jour1"] = 0
	        users[str(user.id)]["b-Mois1"] = 0
	        users[str(user.id)]["b-Annee1"] = 0
	        users[str(user.id)]["b-Heure1"] = 0
	        users[str(user.id)]["b-Minute1"] = 0

	    with open("bans.json", "w") as f:
	        users = json.dump(users, f, indent = 2)
	    return True


def setup(bot):
  	bot.add_cog(Reset(bot))