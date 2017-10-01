from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage, TextMessage

from .methods import *

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(settings.LINE_CHANNEL_SECRET)

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    inputText = event.message.text
    textArray = inputText.lower().split()
    if 'semangatin' in textArray:
        semangat(event, line_bot_api)
    if textArray[0] == 'apakah':
        yesOrNo(event, line_bot_api, textArray)
    if textArray[0] == 'hitung':
        hitung(event, line_bot_api, textArray)

##handler for any other events
##
##@handler.default()
##def default(event):
##    print(event)
##    line_bot_api.reply_message(
##        event.reply_token,
##        TextSendMessage(text='Halo')
##    )


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
