import discord
from discord.ext import commands

class SupportOperations(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def show_support_menu(self, interaction: discord.Interaction):
        support_menu_embed = discord.Embed(
            title="🎯 Support Operations",
            description=(
                "Please select an operation:\n\n"
                "**Available Operations**\n"
                "━━━━━━━━━━━━━━━━━━━━━━\n"
                "📝 **Request Support**\n"
                "└ Get help and support\n\n"
                "👨‍💻 **Developer About**\n"
                "└ Developer information\n"
                "━━━━━━━━━━━━━━━━━━━━━━"
            ),
            color=discord.Color.blue()
        )

        view = SupportView(self)

        try:
            await interaction.response.edit_message(embed=support_menu_embed, view=view)
        except discord.errors.InteractionResponded:
            await interaction.message.edit(embed=support_menu_embed, view=view)

    async def show_support_info(self, interaction: discord.Interaction):
        support_embed = discord.Embed(
            title="🤖 Bot Support Information",
            description=(
                "Hello! If you need help with the bot or are experiencing any issues, "
                "you can always contact me.\n\n"
                "**Developer:** [Click Here](https://discord.gg/e5YgqvZa)\n"
                "Our bot's source code is always 100% open source. "
                "This bot was created and published by UtkarshSharma for free and "
                "**WILL ALWAYS BE FREE.**\n\n"
                "If you would like to support us\n"
                "[☕ Buy me a coffee](https://buymeacoffee.com/codewithutkarsh)\n\n"
                "You can always support by clicking this link.\n"
                "Thank you for using my bot.\n"
                "Feel free to contact me anytime for support."
            ),
            color=discord.Color.gold()
        )

        support_embed.set_thumbnail(url="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png")

        try:
            await interaction.response.send_message(embed=support_embed, ephemeral=True)
            try:
                await interaction.user.send(embed=support_embed)
            except discord.Forbidden:
                await interaction.followup.send(
                    "❌ Could not send DM because your DMs are closed!",
                    ephemeral=True
                )
        except Exception as e:
            print(f"Error sending support info: {e}")

class SupportView(discord.ui.View):
    def __init__(self, cog):
        super().__init__()
        self.cog = cog

    @discord.ui.button(
        label="Request Support",
        emoji="📝",
        style=discord.ButtonStyle.primary,
        custom_id="request_support"
    )
    async def support_request_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.cog.show_support_info(interaction)

    @discord.ui.button(
        label="Developer About",
        emoji="👨‍💻",
        style=discord.ButtonStyle.primary,
        custom_id="developer_about"
    )
    async def developer_about_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        about_embed = discord.Embed(
            title="👨‍💻 About the Developer",
            description=(
                "Thank you for clicking this button, as it shows your interest in learning "
                        "about the person behind this bot.\n\n"
                        "**Developer Information**\n"
                        "━━━━━━━━━━━━━━━━━━━━━━\n"
                        "Professional Profile: [LinkedIn](https://www.linkedin.com/in/codewithutkarsh/)\n\n"
            ),
            color=discord.Color.purple()
        )

        about_embed.set_footer(text="Made with ❤️ by Utkarsh Sharma")

        try:
            await interaction.response.send_message(embed=about_embed, ephemeral=True)
            try:
                await interaction.user.send(embed=about_embed)
            except discord.Forbidden:
                await interaction.followup.send(
                    "❌ Could not send DM because your DMs are closed!",
                    ephemeral=True
                )
        except Exception as e:
            print(f"Error sending developer info: {e}")

    @discord.ui.button(
        label="Main Menu",
        emoji="🏠",
        style=discord.ButtonStyle.secondary,
        custom_id="main_menu"
    )
    async def main_menu_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        alliance_cog = self.cog.bot.get_cog("Alliance")
        if alliance_cog:
            try:
                await interaction.message.edit(content=None, embed=None, view=None)
                await alliance_cog.show_main_menu(interaction)
            except discord.errors.InteractionResponded:
                await interaction.message.edit(content=None, embed=None, view=None)
                await alliance_cog.show_main_menu(interaction)

async def setup(bot):
    await bot.add_cog(SupportOperations(bot))
