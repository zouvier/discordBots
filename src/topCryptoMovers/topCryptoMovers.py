import os
import discord
from discord.ext import commands
import requests

TOKEN = 'YOUR_DISCORD_BOT_TOKEN'
API_KEY = 'YOUR_CRYPTO_API_KEY'

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='top_movers', help='Displays the top market movers in the crypto space.')
async def top_movers(ctx, limit=5):
    url = f'https://api.coingecko.com/api/v3/search/trending?api_key={API_KEY}'
    response = requests.get(url)
    data = response.json()

    if not data:
        await ctx.send('Unable to fetch market data. Please try again later.')
        return

    movers = data['coins'][:limit]
    message = 'Top Market Movers:\n\n'

    for i, mover in enumerate(movers):
        coin = mover['item']
        message += f"{i + 1}. {coin['name']} ({coin['symbol'].upper()}) - Price: ${coin['price_btc']} - 24h Change: {coin['percent_change_24h']}%\n"

    await ctx.send(message)

bot.run(TOKEN)