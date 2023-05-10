import os
from loguru import logger
from pyrogram import Client
from dotenv import load_dotenv

load_dotenv()

logger.remove()
logger.add(
    sink=os.sys.stdout,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> - {message}"
)

api_id = os.getenv("api_id")
api_hash = os.getenv("api_hash")
path_to_otc_chats = os.getenv("path_to_otc_chats")
path_to_message_text = os.getenv("path_to_message_text")

with open(path_to_otc_chats, "r", encoding='utf-8') as f:
    chats = [line.strip() for line in f]

with open(path_to_message_text, "r", encoding='utf-8') as f:
    message_text = f.read()


async def sender():
    async with app:
        try:
            for chat in chats:
                message = await app.send_message(chat_id=chat,
                                                 text=message_text)
                logger.info(f"Message sent to chat {message.chat.title}")

        except Exception as e:
            logger.error(f"Error sending message to chat {chat}: {str(e)}")


if __name__ == '__main__':
    app = Client("my_account", api_id, api_hash)
    app.run(sender())
