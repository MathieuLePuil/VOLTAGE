import discord
from discord.ext import commands
from discord_slash import cog_ext

class Latence(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@cog_ext.cog_slash(name = "latence", description = "Affiche la latence de Voltage.")
	async def latence(self, ctx):
		await ctx.send(f"La latence du bot est de {round(self.bot.latency * 1000)}ms.")

def setup(bot):
  	bot.add_cog(Latence(bot))