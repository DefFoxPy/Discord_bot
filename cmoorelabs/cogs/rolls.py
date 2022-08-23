import discord
from discord.ext import commands

class Select(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Blue", emoji='👌', description='Blue role'),
            discord.SelectOption(label="Red", emoji='✨', description='Red role'),
            discord.SelectOption(label="Green", emoji='🎭', description='Green role')
        ]
        super().__init__(placeholder="Choose your team", max_values=1, min_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        name_role = self.values[0]
        user = interaction.user
        
        try:
            for role in interaction.guild.roles:
                if role.name == name_role:
                    await user.add_roles(role)
                    await interaction.response.send_message(content=f"Team {name_role}", ephemeral=True)
        except:
            await interaction.response.send_message(content='No puedo asignarte ese rol', ephemeral=True)

class SelectView(discord.ui.View):
    def __init__(self, *, timeout=30):
        super().__init__(timeout=timeout)
        self.add_item(Select())

class Role(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('rolls cod loaded.')

    @commands.command()
    async def role(self, ctx):
        await ctx.send("Pick a role", view=SelectView(), delete_after=30)

async def setup(bot):
    await bot.add_cog(Role(bot))