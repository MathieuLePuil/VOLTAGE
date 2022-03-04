import discord
from discord.ext import commands
import json
import datetime
import asyncio
from discord_slash import cog_ext


def convert(time):

    pos = ["s", "m", "h", "d"]

    time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600 * 24}

    unit = time[-1]

    if unit not in pos:
        return -1

    try:
        val = int(time[:-1])
    except:
        return -2

    return val * time_dict[unit]


async def get_prison_data():
    with open("/home/mmi21b12/DISCORD/VOLTAGE/prisons.json", "r") as f:
        users = json.load(f)

    return users


async def first_prison(user):

    users = await get_prison_data()
    name = f"{user.name}#{user.discriminator}"

    if str(user.id) in users:
        return False
    else:

        users[str(user.id)] = {}
        users[str(user.id)]["user_name"] = name
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

    with open("/home/mmi21b12/DISCORD/VOLTAGE/prisons.json", "w") as f:
        json.dump(users, f, indent=2)
    return True


class Prison(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="prison", description="Emprisonne un utilisateur.")
    @commands.has_permissions(kick_members=True)
    async def prison(self, ctx, user: discord.Member, duree, *, reason="Aucune raison n'a été renseignée!"):

        guild = self.bot.get_guild(705089080693751850)
        prisonRole = guild.get_role(752831992374231111)
        acheteurRole = guild.get_role(705096209076977726)

        log_channel = self.bot.get_channel(853703546028818443)
        sanc_channel = self.bot.get_channel(752849744367190016)

        await first_prison(user)
        users = await get_prison_data()
        date = datetime.datetime.now()
        time = convert(duree)

        em = discord.Embed(description=f"**{user}** a été emprisonné **{duree}**! \n \n **Raison:** {reason}",
                           color=0xC15200)
        em.set_thumbnail(url=user.avatar_url)

        try:

            if users[str(user.id)]["1ere Prison"] == "Aucune":
                users[str(user.id)]["1ere Prison"] = reason
                users[str(user.id)]["p-Jour1"] = date.day
                users[str(user.id)]["p-Mois1"] = date.month
                users[str(user.id)]["p-Annee1"] = date.year
                users[str(user.id)]["p-Heure1"] = date.hour
                users[str(user.id)]["p-Minute1"] = date.minute
                users[str(user.id)]["p-Duree1"] = duree
                await ctx.send(embed=em)
                await log_channel.send(embed=em)
                await sanc_channel.send(embed=em)
            elif users[str(user.id)]["1ere Prison"] != "Aucune" and users[str(user.id)]["2eme Prison"] == "Aucune":
                users[str(user.id)]["2eme Prison"] = reason
                users[str(user.id)]["p-Jour2"] = date.day
                users[str(user.id)]["p-Mois2"] = date.month
                users[str(user.id)]["p-Annee2"] = date.year
                users[str(user.id)]["p-Heure2"] = date.hour
                users[str(user.id)]["p-Minute2"] = date.minute
                users[str(user.id)]["p-Duree2"] = duree
                await ctx.send(embed=em)
                await log_channel.send(embed=em)
                await sanc_channel.send(embed=em)
            elif users[str(user.id)]["2eme Prison"] != "Aucune":
                em1 = discord.Embed(description=f"Le joueur {user.name} a déjà reçu 2 peines de prison.",
                                    color=0xC15200)
                await ctx.send(embed=em1)
                return

        except KeyError:
            print("Il y a une erreur!")

        with open("/home/mmi21b12/DISCORD/VOLTAGE/prisons.json", "w") as f:
            json.dump(users, f, indent=2)

        await user.add_roles(prisonRole)
        await user.remove_roles(acheteurRole)

        if duree != "permanent":
            await asyncio.sleep(time)

            await user.remove_roles(prisonRole)
            await user.add_roles(acheteurRole)
            await ctx.send(f"{user.mention} a été évadé!")

        if duree != "perma":
            await asyncio.sleep(time)

            await user.remove_roles(prisonRole)
            await user.add_roles(acheteurRole)
            await ctx.send(f"{user.mention} a été évadé!")

        if duree != "perm":

            await asyncio.sleep(time)

            await user.remove_roles(prisonRole)
            await user.add_roles(acheteurRole)
            await ctx.send(f"{user.mention} a été évadé!")

        else:
            return


def setup(bot):
    bot.add_cog(Prison(bot))
