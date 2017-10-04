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
    elif ('ooh' in textArray) and ('wee' in textArray):
        ooh_wee(event, line_bot_api)
    elif ('wadadaw' in textArray) or ('wadadaaw' in textArray):
        wadadaw(event, line_bot_api)
    elif '*push*' in textArray:
        meeseeks(event, line_bot_api)
    elif 'trigger_timer' in textArray:
        trigger_timer(event, line_bot_api, textArray[1])
    elif '/new' in textArray:
        new_tugas(event, line_bot_api, textArray[1], textArray[2], textArray[3])
    elif ('/task' in textArray[0]) and ('date' in textArray[1]):
        get_tugasInTanggal(event, line_bot_api, textArray[2])
    elif ('/task' in textArray[0]) and ('course' in textArray[1]):
        get_tugasInMatkul(event, line_bot_api, textArray[2])
    elif '/course' in textArray:
        get_courses(event, line_bot_api)
    elif '/remove' in textArray:
        remove_tugas(event, line_bot_api, textArray[1], textArray[2])
    elif '/dictio' in textArray:
        dictio(event, line_bot_api)
    ##TODO implement remind_me, data type = dictionary{nama:tanggal}

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
