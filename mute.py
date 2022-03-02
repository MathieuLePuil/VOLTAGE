import discord
from discord.ext import commands
import json
import datetime
import asyncio
from discord_slash import cog_ext



class Mute(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	def convert(self, time):

		pos = ["s","m","h","d"]

		time_dict = {"s" : 1, "m" : 60, "h" : 3600, "d": 3600*24}

		unit = time[-1]

		if unit not in pos:
			return -1

		try:
			val = int(time[:-1])
		except:
			return -2

		return val * time_dict[unit]


	async def createMuteRole(self, ctx):
		muteRole = await ctx.guild.create_role(name = "Muted",
			reason = "Création d'un Blacklist pour les giveaways")
		for channel in ctx.guild.channels:
			await channel.set_permissions(muteRole, send_messages = False, speak = True)
			return muteRole

		return await createMuteRole(self, ctx)

	def getMuteRole(self, ctx):
		roles = ctx.guild.roles
		for role in roles:
			if role.name == "Muted":
				return role
	

	@cog_ext.cog_slash(name = "mute", description = "Rend muet un utilisateur.")
	@commands.has_permissions(kick_members = True)
	async def mute(self, ctx, user : discord.Member, duree, *, reason = "Aucune raison n'a été renseignée!"):

		log_channel = self.bot.get_channel(853703546028818443)

		await self.first_mute(user)
		users = await self.get_mute_data()
		muteRole = self.getMuteRole(ctx)
		time = self.convert(duree)
		date = datetime.datetime.now()

		em = discord.Embed(description = f"**{user}** a été mute **{duree}**! \n \n **Raison:** {reason}", color = 0xC15200)
		em.set_thumbnail(url = user.avatar_url)


		try:

			if users[str(user.id)]["1er Mute"] == "Aucune":
				users[str(user.id)]["1er Mute"] = reason
				users[str(user.id)]["m-Jour1"] = date.day
				users[str(user.id)]["m-Mois1"] = date.month
				users[str(user.id)]["m-Annee1"] = date.year
				users[str(user.id)]["m-Heure1"] = date.hour
				users[str(user.id)]["m-Minute1"] = date.minute
				users[str(user.id)]["m-Duree1"] = duree
				await ctx.send(embed = em)
				await log_channel.send(embed = em)
			elif users[str(user.id)]["1er Mute"] != "Aucune" and users[str(user.id)]["2eme Mute"] == "Aucune":
				users[str(user.id)]["2eme Mute"] = reason
				users[str(user.id)]["m-Jour2"] = date.day
				users[str(user.id)]["m-Mois2"] = date.month
				users[str(user.id)]["m-Annee2"] = date.year
				users[str(user.id)]["m-Heure2"] = date.hour
				users[str(user.id)]["m-Minute2"] = date.minute
				users[str(user.id)]["m-Duree2"] = duree
				await ctx.send(embed = em)
				await log_channel.send(embed = em)
			elif users[str(user.id)]["2eme Mute"] != "Aucune":
				em1 = discord.Embed(description = f"Le joueur {user.name} a déjà reçu 2 mutes.", color = 0xC15200)
				await ctx.send(embed = em1)
				return

		except KeyError:
			print(f"Il y a une erreur!")

		with open("mutes.json", "w") as f:
			users = json.dump(users, f, indent = 2)

		await user.add_roles(muteRole)

		if duree != "permanent":
		
			await asyncio.sleep(time)

			await user.remove_roles(muteRole)
			await ctx.send(f"{user.mention} a été unmute!")
			return

		if duree != "perma":

			await asyncio.sleep(time)

			await user.remove_roles(muteRole)
			await ctx.send(f"{user.mention} a été unmute!")
			return

		if duree != "perm":

			await asyncio.sleep(time)

			await user.remove_roles(muteRole)
			await ctx.send(f"{user.mention} a été unmute!")
			return

		else:
			return

	@cog_ext.cog_slash(name = "unmute", description = "Redonne la parole à l'utilisateur.")
	@commands.has_permissions(kick_members = True)
	async def unmute(self, ctx, user : discord.Member):

		muteRole = self.getMuteRole(ctx)
		await user.remove_roles(muteRole)

		em1 = discord.Embed(description = f"{user} a été unmute!", color = 0xC15200)
		await ctx.send(embed = em1)



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

	async def get_mute_data(self):
	    with open("mutes.json", "r") as f:
	        users = json.load(f)

	    return users


def setup(bot):
  	bot.add_cog(Mute(bot))