from discord.ext import commands
from config import get_section
from discord import *


class reactionranker(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.channel_id == int(get_section("bot").get("rank_channel_id")):
            discorduser = utils.get(Client.get_all_members(self.bot), id=payload.user_id)
            await discorduser.add_roles(utils.get(discorduser.guild.roles, id=int(get_section("bot").get("ranks").get(payload.emoji.id))))

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if payload.channel_id == int(get_section("bot").get("rank_channel_id")):
            discorduser = utils.get(Client.get_all_members(self.bot), id=payload.user_id)
            if utils.get(discorduser.guild.roles, id=int(get_section("bot").get("ranks").get(payload.emoji.id))) in discorduser.roles:
                await discorduser.remove_roles(utils.get(discorduser.guild.roles, id=int(get_section("bot").get("ranks").get(payload.emoji.id))))


def setup(bot):
    bot.add_cog(reactionranker(bot))
