from twitchio.ext import commands

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            token='oauth:YOUR_OAUTH_TOKEN',      # Fill with your bot's OAuth token
            prefix='!',
            initial_channels=['your_channel']     # Replace with your channel name
        )

    async def event_ready(self):
        print(f"Logged in as | {self.nick}")

    async def event_message(self, message):
        if message.echo:
            return
        await self.handle_commands(message)

    @commands.command(name='hello')
    async def hello(self, ctx):
        await ctx.send(f'Hello @{ctx.author.name}! I am a live interactive bot.')

bot = Bot()
bot.run()
