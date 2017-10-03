from linebot.models import *
from lxml import html
import time
import requests
import random
import sys

semangat_list = ['Semangat cuy!', 'Lo pasti bisa!', 'Pasti sukses', 'Good luck!',\
                 'Apa sih yang lo ga bisa?', 'Jangan putus asa, masih ada harapan']

letter_weight = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,\
                 'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,\
                 's':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}

ultah = {'Yuris':'02/10/2017'}

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
    main_url = 'https://www.bitcoin.co.id/'
    req = requests.get(main_url)
    tree = html.fromstring(req.content)
    harga = tree.xpath('//div[@class="pull-right"]/span/text()')
    harga = (harga[0].split())[3]
    jam = int(time.strftime('%H')) + 7
    if(jam > 24):
        jam-=24
        if(jam < 10): jam = '0'+str(jam)
    menit = time.strftime('%M')
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='1 BTC = Rp. {}\n.\nChecked on {} at {}:{}'.format(harga,time.strftime("%d/%m/%Y"),jam,menit))
    )

def button(event, line_bot_api):
    buttons_template_message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            thumbnail_image_url='https://i.imgur.com/BIDxujA.png',
            title='Menu',
            text='Please select',
            actions=[
                PostbackTemplateAction(
                    label='postback',
                    text='postback text',
                    data='action=buy&itemid=1'
                ),
                MessageTemplateAction(
                    label='message',
                    text='message text'
                ),
                URITemplateAction(
                    label='uri',
                    uri='http://example.com/'
                )
            ]
        )
    )
    line_bot_api.reply_message(
        event.reply_token,
        buttons_template_message
    )

def groupid(event, line_bot_api):
    print(event.source.group_id)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.source.group_id)
    )
    
def get_name(event, line_bot_api):
    if(isinstance(event.source, SourceUser)):
        userId = event.source.sender_id
        profile = line_bot_api.get_profile(userId)
        name = profile.display_name
    elif(isinstance(event.source, SourceGroup)):
        groupId = event.source.group_id
        userId = event.source.user_id
        profile = line_bot_api.get_group_member_profile(groupId, userId)
        name = profile.display_name
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=name)
    )

def ooh_wee(event, line_bot_api):
    audio_message = AudioSendMessage(
        original_content_url='https://drive.google.com/uc?export=download&id=0B_pg-_BXUdGrdGxIWGFsTWVXUDA',
        duration=1000
    )
    line_bot_api.reply_message(
        event.reply_token,
        audio_message
    )

