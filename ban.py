import discord
from discord.ext import commands
import datetime
import json
from discord_slash import cog_ext


async def get_ban_data():
    with open("/home/mmi21b12/DISCORD/VOLTAGE/bans.json", "r") as f:
        users = json.load(f)

    return users


async def first_ban(user):

    users = await get_ban_data()
    name = f"{user}"

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

    with open("/home/mmi21b12/DISCORD/VOLTAGE/bans.json", "w") as f:
        json.dump(users, f, indent=2)
    return True


class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="ban", description="Bannis un utilisateur.")
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.User, *, reason="Aucune raison n'a été renseignée!"):

        log_channel = self.bot.get_channel(853703546028818443)

        await first_ban(user)
        users = await get_ban_data()
        date = datetime.datetime.now()

        em = discord.Embed(description=f"**{user}** a été ban! \n \n **Raison:** {reason}", color=0xFF1700)
        em.set_thumbnail(url=user.avatar_url)

        try:

            users[str(user.id)]["1er Ban"] = reason
            users[str(user.id)]["b-Jour1"] = date.day
            users[str(user.id)]["b-Mois1"] = date.month
            users[str(user.id)]["b-Annee1"] = date.year
            users[str(user.id)]["b-Heure1"] = date.hour
            users[str(user.id)]["b-Minute1"] = date.minute
            await ctx.send(embed=em)
            await log_channel.send(embed=em)

        except KeyError:
            print(f"Il y a une erreur!")

        emban = discord.Embed(description=f"⛔ Vous avez été ban du **`ScaryShop`** pour ***{reason}*** !",
                              color=0xFF1700)
        await user.send(embed=emban)

        await ctx.guild.ban(user, reason=reason)

        with open("/home/mmi21b12/DISCORD/VOLTAGE/bans.json", "w") as f:
            json.dump(users, f, indent=2)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, user, *reason):

        userName, userID = user.split("#")
        bannedUsers = await ctx.guild.bans()
        for i in bannedUsers:
            if i.user.name == userName and i.user.discriminator == userID:
                await ctx.guild.unban(i.user, reason=reason)
                em = discord.Embed(description=f"**{user}** a été unban du ScaryShop!", color=0xFF1700)
                await ctx.send(embed=em)
                return
        em1 = discord.Embed(description=f"**{user}** ne figure pas dans la liste des joueurs bannis.", color=0xFF1700)
        await ctx.send(embed=em1)


def setup(bot):
    bot.add_cog(Ban(bot))
