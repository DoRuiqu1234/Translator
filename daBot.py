import discord
from googletrans import Translator
from timeConv import myTimeConverter

client = discord.Client(intents=discord.Intents.all())
translator = Translator()
conv = myTimeConverter()

@client.event
async def on_ready():
    print("Bot is running!")

@client.event
async def on_message(message):
    # No Repeating
    if message.author == client.user:
        return
    # discord.Message.
    text = message.content
    if text.startswith('!clear'):
        if message.author.guild_permissions.manage_messages: 
            if len(text.split(' ')) == 1:
                await message.channel.purge(limit=1000000)
            else:
                amount = text.split(' ')[1]
                try:
                    int(amount)
                except: # Error handler
                    await message.channel.send('Please enter a valid integer as amount.')
                else:
                    await message.channel.purge(limit=int(amount))
                    await message.channel.send(f'Pro master 🗿 {message.author.mention} deleted {amount} messages!')
        else:
            await message.channel.send('you aint got no permission boi')
    if text.startswith('!time'):
        if len(text.split(' ')) == 1:
            await message.channel.send(conv.get(-1))
        else:
            await message.channel.send(conv.get(' '.join(text.split(' ')[1:])))
    if message.channel.id != 1149512881289838653:
        lang = translator.detect(text).lang
        if lang != 'en':
            await client.get_channel(1149512881289838653).send(f"({lang})[{str(message.author)}]: "+translator.translate(text).text)


client.run(token here | private)