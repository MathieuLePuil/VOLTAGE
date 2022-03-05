from discord.ext import commands
from discord_slash import cog_ext


class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="clear", description="Supprime un certain nombre de message.")
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, number: int):
        await ctx.channel.purge(limit=number, check=lambda msg: not msg.pinned)
        if number != 1:
            await ctx.send(f"<a:scarycheck:835499517977690122>  **`{number}` messages ont été supprimés.**",
                           delete_after=5)
        elif number == 1:
            await ctx.send(f"<a:scarycheck:835499517977690122>  **`{number}` message a été supprimé.**", delete_after=5)
        else:
            await ctx.send(f"<a:scarywrong:835499521341128746>  **Il n'y a aucun messages à supprimer.**\n",
                           delete_after=5)


def setup(bot):
    bot.add_cog(Clear(bot))
