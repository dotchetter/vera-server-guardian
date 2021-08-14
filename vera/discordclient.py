import discord
from pyttman.clients.community.discord.client import DiscordClient


class CustomDiscordClient(DiscordClient):

    async def on_member_join(self, member: discord.Member) -> None:
        """
        If a new member just joined our server, greet them warmly!
        """
        await member.create_dm()
        await member.dm_channel.send(f"Welcome to the Pyttman Discord server,"
                                     f"{member} :smiley: **I'm Vera**, the "
                                     f"guardian of the Discord server for Pyttman. "
                                     f"I'll post news about Pyttman and keep the "
                                     f"server clean. See you around!")