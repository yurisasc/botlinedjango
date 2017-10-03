from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage, TextMessage

from .methods import *
from datetime import datetime, timedelta

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(settings.LINE_CHANNEL_SECRET)


##dictionary tanggal ultah anak-anak
ultah = {'Yuris':'02/10/2017'}
@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    inputText = event.message.text
    textArray = inputText.lower().split()
    if 'semangatin' in textArray:
        semangat(event, line_bot_api)
    elif textArray[0] == 'apakah':
        yesOrNo(event, line_bot_api, textArray)
    elif textArray[0] == 'hitung':
        hitung(event, line_bot_api, inputText.lower().split(' ', 1))
    elif 'astaghfirullah' in textArray:
        meme_astaghfirullah(event, line_bot_api)
    elif ('activate' in textArray) and ('trap' in textArray):
        meme_trapSeto(event, line_bot_api)
    elif ('harga' in textArray) and ('bitcoin' in textArray):
        scrape_btc(event, line_bot_api)
    elif 'button' in textArray:
        button(event, line_bot_api)
    elif 'name' in textArray:
        get_name(event, line_bot_api)
    elif 'groupid' in textArray:
        groupid(event, line_bot_api)
    ##TODO implement remind_me, data type = dictionary{nama:tanggal}

while(True):
    for key in ultah.keys(): 
        if time.strftime("%d/%m/%Y") in ultah.get(key):
            print("debug 1s")
    time.sleep(1)

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()
        return HttpResponse()
    else:
        return HttpResponseBadRequest()
