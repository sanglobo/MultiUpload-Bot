import os

class Config(object):
   # The Telegram API things
   API_ID= int(os.environ.get("API_ID", 27885485))
   API_HASH = os.environ.get("API_HASH", "7dd9974c713787410beae4a295cc1e2d" )
   # get a token from @BotFather
   BOT_TOKEN = os.environ.get("BOT_TOKEN", "5836338648:AAG-zGTyl1ZcuJ8CMhDFlImrOIjxTSH1YQ0")
   # channel id = -100 (for logs)
   LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001979868216"))   
   # Array to store users who are authorized to use the bot 
   AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5663539940").split())    
   # force sub user to the channel (without @)
   CHNAME = os.environ.get("CHNAME", "teste680")
