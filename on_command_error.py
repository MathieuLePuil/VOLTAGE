from discord.ext import commands


class On_command_error(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("Vous n'avez pas la permission d'effectuer cette commande.", delete_after=5)

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Il manque un argumement à la commande!", delete_after=5)


def setup(bot):
    bot.add_cog(On_command_error(bot))
