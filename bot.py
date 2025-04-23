import discord
import requests
import os
from datetime import date
from dotenv import load_dotenv

print("🚀 Starting bot.py...")  # Debug print to confirm script runs

load_dotenv()

API_KEY = os.getenv("NASA_API_KEY")
BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
NASA_URL = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"

intents = discord.Intents.default()
intents.message_content = True  # Allow bot to read messages

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'🛰️  Logged in as {client.user}')


@client.event
async def on_message(message):
    print(f"Received message: {message.content}")

    if message.author == client.user:
        return  # Don't respond to itself

    if message.content.startswith("!space"):
        print("✅ Received !space command!")

        # Fetch NASA APOD data
        response = requests.get(NASA_URL)
        print(f"API response: {response.status_code}")
        data = response.json()

        if data['media_type'] != 'image':
            await message.channel.send("🚫 Today's APOD is a video, not an image.")
            return

        # Download image
        title = data['title']
        explanation = data['explanation']
        img_url = data.get('hdurl', data['url'])

        today = date.today().isoformat()
        file_path = f"nasa_wallpapers/{today}.jpg"
        os.makedirs("nasa_wallpapers", exist_ok=True)

        img_data = requests.get(img_url).content
        with open(file_path, 'wb') as handler:
            handler.write(img_data)
        print(f"✅ Saved image to {file_path}")


        from datetime import datetime
        # Format the date into APOD's specific URL format
        apod_date = datetime.strptime(data['date'], "%Y-%m-%d")
        apod_page_url = f"https://apod.nasa.gov/apod/ap{apod_date.strftime('%y%m%d')}.html"


        # Create embed with image as attachment
        embed = discord.Embed(
            title=title,
            url=apod_page_url,  # 🔗 makes the title a clickable link!
            description=explanation[:500] + "...",
            color=0x1e90ff
        )
        embed.set_image(url=f"attachment://{today}.jpg")
        embed.set_footer(text=f"Date: {data['date']} | NASA APOD")

        with open(file_path, 'rb') as f:
            await message.channel.send(
                content="🌌 Here's today's Astronomy Picture of the Day!",
                embed=embed,
                file=discord.File(f, filename=f"{today}.jpg")
            )

        print("✅ APOD posted and image sent!")


client.run(BOT_TOKEN)
