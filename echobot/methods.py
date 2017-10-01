from linebot.models import TextSendMessage
import random

semangat_list = ['Semangat cuy!', 'Lo pasti bisa!', 'Pasti sukses', 'Good luck!',\
                 'Apa sih yang lo ga bisa?', 'Jangan putus asa, masih ada harapan']

def semangat(event, line_bot_api):
    line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=semangat_list[random.randint(len(semangat_list) - 1)])
        )
