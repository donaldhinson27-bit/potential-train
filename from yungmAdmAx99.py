from yungmAdmAx99.ext import commands



bot=commands.bot
    irc_token=f2wh6h4sh7n89tyshphgfljc6vvdoz
    client_id='74yqjc0tnhexakaa0t5axc7lwnigsd',
    nick='potential-train ',
    prefix='!',
    initial_channels=['yungmAdmAx99']



)@bot.event
async def event_ready():
    print(f'yungmAdmAx99 is online!')
async def event_message(ctx):
    if ctx.author.name.lower() == 'yungmAdmAx99':
        await ctx.channel.send(f'Hello {ctx.author.name}!')
    await bot.handle_commands(ctx)
    bot=run



if __name__ == "__main__":
    