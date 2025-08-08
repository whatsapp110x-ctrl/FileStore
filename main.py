from bot import Bot
import pyrogram.utils
from keep_alive import keep_alive  # Added

pyrogram.utils.MIN_CHANNEL_ID = -1009147483647

if __name__ == "__main__":
    keep_alive()  # Start the web server
    Bot().run()
