from linebot.models import TextSendMessage, ImageSendMessage
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import sys

semangat_list = ['Semangat cuy!', 'Lo pasti bisa!', 'Pasti sukses', 'Good luck!',\
                 'Apa sih yang lo ga bisa?', 'Jangan putus asa, masih ada harapan']

letter_weight = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,\
                 'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,\
                 's':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}

def semangat(event, line_bot_api):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=semangat_list[random.randint(0, len(semangat_list)-1)])
    )

def yesOrNo(event, line_bot_api, textArray):
    weight = 0
    for words in textArray[1:]:
        for char in words:
            if char in letter_weight:
                weight += letter_weight[char]
    if weight%2 == 1:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='ya')
        )
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='nggak')
        )

def hitung(event, line_bot_api, textArray):
    try:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=eval(textArray[1]))
        )
    except:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='Input angka yang bener ya')
        )

def meme_astaghfirullah(event, line_bot_api):
    image_message = ImageSendMessage(
        original_content_url='https://i.imgur.com/2PjT87u.jpg',
        preview_image_url='https://i.imgur.com/2PjT87u.jpg'
    )
    line_bot_api.reply_message(
        event.reply_token,
        image_message
    )        

def meme_trapSeto(event, line_bot_api):
    image_message = ImageSendMessage(
        original_content_url='https://i.imgur.com/giz4DiI.jpg',
        preview_image_url='https://i.imgur.com/giz4DiI.jpg'
    )
    line_bot_api.reply_message(
        event.reply_token,
        image_message
    )        

def scrape_btc(event, line_bot_api):
    selenium = webdriver.Chrome()
    selenium.get('https://www.google.co.id/search?hl=en&source=hp&q=1+btc+to+idr&oq=&gs_l=psy-ab.1.1.35i39k1l6.0.0.0.17304.8.1.6.0.0.0.0.0..1.0.dummy_maps_web_fallback...0...1..64.psy-ab..1.7.161.6...117.FYi5o41hMbk')
    btc = selenium.find_element_by_id('pair_targ_input')
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=btc)
    )
