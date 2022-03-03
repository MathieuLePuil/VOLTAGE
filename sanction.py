import discord
from discord.ext import commands
import json
from discord_slash import cog_ext


class Sanction(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="sanction", description="Affiche la liste des sanctions d'un utilisateur.")
    async def sanction(self, ctx, sanction_type, user: discord.User):

        if sanction_type == "warn":
            await self.first_warn(user)
            users = await self.get_warn_data()

            sanction_1 = users[str(user.id)]["1er Warn"]
            jour_1 = users[str(user.id)]["w-Jour1"]
            mois_1 = users[str(user.id)]["w-Mois1"]
            annee_1 = users[str(user.id)]["w-Annee1"]
            heure_1 = users[str(user.id)]["w-Heure1"]
            minute_1 = users[str(user.id)]["w-Minute1"]
            sanction_2 = users[str(user.id)]["2eme Warn"]
            jour_2 = users[str(user.id)]["w-Jour2"]
            mois_2 = users[str(user.id)]["w-Mois2"]
            annee_2 = users[str(user.id)]["w-Annee2"]
            heure_2 = users[str(user.id)]["w-Heure2"]
            minute_2 = users[str(user.id)]["w-Minute2"]

            em1 = discord.Embed(description=f"Le joueur {user.name} n'a reçu aucun warn!", color=0xFF6C00)
            em2 = discord.Embed(title=f"Liste des warns de {user.name}",
                                description=f"> • Warn le **{jour_1}/{mois_1}/{annee_1}** à *{heure_1}h{minute_1}* pour **{sanction_1}**",
                                color=0xFF6C00)
            em3 = discord.Embed(title=f"Liste des warns de {user.name}",
                                description=f"> • Warn le **{jour_1}/{mois_1}/{annee_1}** à *{heure_1}h{minute_1}* pour **{sanction_1}** \n > • Warn le **{jour_2}/{mois_2}/{annee_2}** à *{heure_2}h{minute_2}* pour **{sanction_2}**",
                                color=0xFF6C00)

            if users[str(user.id)]["1er Warn"] == "Aucune":
                await ctx.send(embed=em1)
            elif users[str(user.id)]["1er Warn"] != "Aucune" and users[str(user.id)]["2eme Warn"] == "Aucune":
                await ctx.send(embed=em2)
            elif users[str(user.id)]["1er Warn"] != "Aucune" and users[str(user.id)]["2eme Warn"] != "Aucune":
                await ctx.send(embed=em3)

        elif sanction_type == "mute":
            await self.first_mute(user)
            users = await self.get_mute_data()

            sanction_1 = users[str(user.id)]["1er Mute"]
            jour_1 = users[str(user.id)]["m-Jour1"]
            mois_1 = users[str(user.id)]["m-Mois1"]
            annee_1 = users[str(user.id)]["m-Annee1"]
            heure_1 = users[str(user.id)]["m-Heure1"]
            minute_1 = users[str(user.id)]["m-Minute1"]
            duree_1 = users[str(user.id)]["m-Duree1"]
            sanction_2 = users[str(user.id)]["2eme Mute"]
            jour_2 = users[str(user.id)]["m-Jour2"]
            mois_2 = users[str(user.id)]["m-Mois2"]
            annee_2 = users[str(user.id)]["m-Annee2"]
            heure_2 = users[str(user.id)]["m-Heure2"]
            minute_2 = users[str(user.id)]["m-Minute2"]
            duree_2 = users[str(user.id)]["m-Duree2"]

            em1 = discord.Embed(description=f"Le joueur {user.name} n'a reçu aucun mute!", color=0xFF6C00)
            em2 = discord.Embed(title=f"Liste des mutes de {user.name}",
                                description=f"> • Mute le **{jour_1}/{mois_1}/{annee_1}** à *{heure_1}h{minute_1}* pendant ***{duree_1}*** pour **{sanction_1}**",
                                color=0xFF6C00)
            em3 = discord.Embed(title=f"Liste des warns de {user.name}",
                                description=f"> • Mute le **{jour_1}/{mois_1}/{annee_1}** à *{heure_1}h{minute_1}* pendant ***{duree_1}*** pour **{sanction_1}** \n > • Mute le **{jour_2}/{mois_2}/{annee_2}** à *{heure_2}h{minute_2}* pendant ***{duree_2}*** pour **{sanction_2}**",
                                color=0xFF6C00)

            if users[str(user.id)]["1er Mute"] == "Aucune":
                await ctx.send(embed=em1)
            elif users[str(user.id)]["1er Mute"] != "Aucune" and users[str(user.id)]["2eme Mute"] == "Aucune":
                await ctx.send(embed=em2)
            elif users[str(user.id)]["1er Mute"] != "Aucune" and users[str(user.id)]["2eme Mute"] != "Aucune":
                await ctx.send(embed=em3)

        elif sanction_type == "kick":
            await self.first_kick(user)
            users = await self.get_kick_data()

            sanction_1 = users[str(user.id)]["1er Kick"]
            jour_1 = users[str(user.id)]["k-Jour1"]
            mois_1 = users[str(user.id)]["k-Mois1"]
            annee_1 = users[str(user.id)]["k-Annee1"]
            heure_1 = users[str(user.id)]["k-Heure1"]
            minute_1 = users[str(user.id)]["k-Minute1"]
            sanction_2 = users[str(user.id)]["2eme Kick"]
            jour_2 = users[str(user.id)]["k-Jour2"]
            mois_2 = users[str(user.id)]["k-Mois2"]
            annee_2 = users[str(user.id)]["k-Annee2"]
            heure_2 = users[str(user.id)]["k-Heure2"]
            minute_2 = users[str(user.id)]["k-Minute2"]

            em1 = discord.Embed(description=f"Le joueur {user.name} n'a reçu aucun kick!", color=0xFF6C00)
            em2 = discord.Embed(title=f"Liste des kicks de {user.name}",
                                description=f"> • Kick le **{jour_1}/{mois_1}/{annee_1}** à *{heure_1}h{minute_1}* pour **{sanction_1}**",
                                color=0xFF6C00)
            em3 = discord.Embed(title=f"Liste des warns de {user.name}",
                                description=f"> • Kick le **{jour_1}/{mois_1}/{annee_1}** à *{heure_1}h{minute_1}* pour **{sanction_1}** \n > • Kick le **{jour_2}/{mois_2}/{annee_2}** à *{heure_2}h{minute_2}* pour **{sanction_2}**",
                                color=0xFF6C00)

            if users[str(user.id)]["1er Kick"] == "Aucune":
                await ctx.send(embed=em1)
            elif users[str(user.id)]["1er Kick"] != "Aucune" and users[str(user.id)]["2eme Kick"] == "Aucune":
                await ctx.send(embed=em2)
            elif users[str(user.id)]["1er Kick"] != "Aucune" and users[str(user.id)]["2eme Kick"] != "Aucune":
                await ctx.send(embed=em3)


        elif sanction_type == "prison":
            await self.first_prison(user)
            users = await self.get_prison_data()

            sanction_1 = users[str(user.id)]["1ere Prison"]
            jour_1 = users[str(user.id)]["p-Jour1"]
            mois_1 = users[str(user.id)]["p-Mois1"]
            annee_1 = users[str(user.id)]["p-Annee1"]
            heure_1 = users[str(user.id)]["p-Heure1"]
            minute_1 = users[str(user.id)]["p-Minute1"]
            duree_1 = users[str(user.id)]["p-Duree1"]
            sanction_2 = users[str(user.id)]["2eme Prison"]
            jour_2 = users[str(user.id)]["p-Jour2"]
            mois_2 = users[str(user.id)]["p-Mois2"]
            annee_2 = users[str(user.id)]["p-Annee2"]
            heure_2 = users[str(user.id)]["p-Heure2"]
            minute_2 = users[str(user.id)]["p-Minute2"]
            duree_2 = users[str(user.id)]["p-Duree2"]

            em1 = discord.Embed(description=f"Le joueur {user.name} n'a reçu aucune peine de prison!", color=0xFF6C00)
            em2 = discord.Embed(title=f"Liste des emprisonnements de {user.name}",
                                description=f"> • Emprisonné le **{jour_1}/{mois_1}/{annee_1}** à *{heure_1}h{minute_1}* pendant ***{duree_1}*** pour **{sanction_1}**",
                                color=0xFF6C00)
            em3 = discord.Embed(title=f"Liste des warns de {user.name}",
                                description=f"> • Emprisonné le **{jour_1}/{mois_1}/{annee_1}** à *{heure_1}h{minute_1}* pendant ***{duree_1}*** pour **{sanction_1}** \n > • Emprisonné le **{jour_2}/{mois_2}/{annee_2}** à *{heure_2}h{minute_2}* pendant ***{duree_2}*** pour **{sanction_2}**",
                                color=0xFF6C00)

            if users[str(user.id)]["1ere Prison"] == "Aucune":
                await ctx.send(embed=em1)
            elif users[str(user.id)]["1ere Prison"] != "Aucune" and users[str(user.id)]["2eme Prison"] == "Aucune":
                await ctx.send(embed=em2)
            elif users[str(user.id)]["1ere Prison"] != "Aucune" and users[str(user.id)]["2eme Prison"] != "Aucune":
                await ctx.send(embed=em3)


        else:
            em = discord.Embed(
                description=f"**{sanction_type}** n'exite pas. Merci d'entrer `warn` | `mute` | `prison`| `kick`.",
                color=0xFF6C00)
            await ctx.send(embed=em)

    async def get_warn_data(self):
        with open("/home/mmi21b12/DISCORD/VOLTAGE/warns.json", "r") as f:
            users = json.load(f)

        return users

    async def get_mute_data(self):
        with open("/home/mmi21b12/DISCORD/VOLTAGE/mutes.json", "r") as f:
            users = json.load(f)

        return users

    async def get_kick_data(self):
        with open("/home/mmi21b12/DISCORD/VOLTAGE/kicks.json", "r") as f:
            users = json.load(f)

        return users

    async def get_prison_data(self):
        with open("/home/mmi21b12/DISCORD/VOLTAGE/prisons.json", "r") as f:
            users = json.load(f)

        return users

    async def get_ban_data(self):
        with open("/home/mmi21b12/DISCORD/VOLTAGE/bans.json", "r") as f:
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

        with open("/home/mmi21b12/DISCORD/VOLTAGE/warns.json", "w") as f:
            users = json.dump(users, f, indent=2)
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

        with open("/home/mmi21b12/DISCORD/VOLTAGE/mutes.json", "w") as f:
            users = json.dump(users, f, indent=2)
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

        with open("/home/mmi21b12/DISCORD/VOLTAGE/kicks.json", "w") as f:
            users = json.dump(users, f, indent=2)
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

        with open("/home/mmi21b12/DISCORD/VOLTAGE/prisons.json", "w") as f:
            users = json.dump(users, f, indent=2)
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

        with open("/home/mmi21b12/DISCORD/VOLTAGE/bans.json", "w") as f:
            users = json.dump(users, f, indent=2)
        return True


def setup(bot):
    bot.add_cog(Sanction(bot))
