import discord
from discord.ext import commands
from discord_slash import cog_ext


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="help", description="Affiche toutes les commandes disponibles dans Voltage.")
    async def help(self, ctx):
        em1 = discord.Embed(title="Help Voltage", description="Voici la liste de toutes les commandes disponibles:",
                            color=0x577F3F)
        em1.add_field(name="`/setprefix <Prefix>`", value="<:fad:835500807210270770> Change le prefix sur le serveur.",
                      inline=False)
        em1.add_field(name="`/latence`", value="<:fad:835500807210270770> Afficge la latence du bot.", inline=False)
        em1.add_field(name="`/warn <Mention Utilisateur> <Raison>`",
                      value="<:fad:835500807210270770> Permet d'avertir un utilisateur.", inline=False)
        em1.add_field(name="`/mute <Mention Utilisateur> <Durée s|m|h|d|perm> <Raison>`",
                      value="<:fad:835500807210270770> Empêche l'utilisateur de parler.", inline=False)
        em1.add_field(name="`/prison <Mention Utilisateur> <Durée s|m|h|d|perm> <Raison>`",
                      value="<:fad:835500807210270770> Empêche l'utilisateur d'accéder au serveur.", inline=False)
        em1.add_field(name="`/kick <Mention utilisateur> <Raison>`",
                      value="<:fad:835500807210270770> Expulse l'utilisateur du serveur.", inline=False)
        em1.add_field(name="`/ban <Mention utilisateur> <Raison>`",
                      value="<:fad:835500807210270770> Bannis l'utilisateur du serveur.", inline=False)
        em1.add_field(name="`/reset <warn | mute | prison | kick> <Mention utilisateur>`",
                      value="<:fad:835500807210270770> Retire les sanctions de l'utilisateur.", inline=False)
        em1.add_field(name="`/sanction <warn | mute | prison | kick> <Mention utilisateur>`",
                      value="<:fad:835500807210270770> Affiche les sanctions de l'utilisateur.", inline=False)
        em1.add_field(name="`/clear <Nombre de Message>`",
                      value="<:fad:835500807210270770> Supprime le nombre de message indiqué.", inline=False)
        em1.set_thumbnail(url="https://cdn.discordapp.com/emojis/762020637283713055.png?v=1")
        em1.set_image(url="https://cdn.discordapp.com/emojis/813748552915222529.png?v=1")
        await ctx.send(embed=em1)


def setup(bot):
    bot.add_cog(Help(bot))
