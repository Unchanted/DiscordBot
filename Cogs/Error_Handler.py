import discord
from discord.ext import commands

class Error_Handler(commands.Cog):
    def __init__(self,client: discord.Client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):
        """A global error handler cog."""
        if isinstance(error, commands.CommandNotFound):
            return  # Return because we don't want to show an error for every command not found
        elif isinstance(error, commands.CommandOnCooldown):
            message = f"This command is on cooldown. Please try again after **{round(error.retry_after, 2)}**s."
            await ctx.send(message, delete_after=(round(error.retry_after, 2)))
            return
        elif isinstance(error, commands.MissingPermissions):
            message = f"You do not the required permissions to run this command! You are missing `{error.missing_perms}` Perms"
        # elif isinstance(error, commands.MissingPermissions):
        #     message = "You can't run this command!"
        elif isinstance(error, commands.MissingRequiredArgument):
            message = "You entered less numer of Arguments, please use the command correctly!"
        elif isinstance(error, commands.UserInputError):
            message = "Something about your input was wrong, please check your input and try again!"
        else:
            message = "Oh no! Something went wrong while running the command!"
            await ctx.send(message)
            raise error
            

        await ctx.message.reply(message, mention_author = False)


def setup(client: discord.Client):
    client.add_cog(Error_Handler(client))
