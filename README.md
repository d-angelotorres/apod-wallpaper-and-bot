# APOD Wallpaper & Discord Bot

This project consists of a bot that fetches NASA's Astronomy Picture of the Day (APOD) and posts it to a Discord server. The bot also saves the images to your local machine and sends a daily message with the latest APOD. The `!space` command can be used to fetch and post the image on demand.

## Features

- Posts the latest Astronomy Picture of the Day (APOD) to a Discord channel.
- Saves the image locally to `nasa_wallpapers/`.
- Sends an embedded message with the APOD title, description, and image.
- Must be manually triggered with the `!space` command.

## Setup

1. **Clone the repository**:

   ```
   git clone https://github.com/yourusername/apod-wallpaper-and-bot.git
   cd apod-wallpaper-and-bot
   ```

2. **Create a virtual environment**:

   ```
   python3 -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies**:

   ```
   pip install -r requirements.txt
   ```

4. **Create a `.env` file** and add your NASA API key and Discord Bot token:

   ```
   NASA_API_KEY=your_nasa_api_key_here
   DISCORD_BOT_TOKEN=your_discord_token_here
   ```

5. **Run the bot**:
   ```
   python3 bot.py
   ```

## License

This project is open-source and available under the [MIT License](LICENSE).
