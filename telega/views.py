from django.shortcuts import render
import telebot

def send_message(request):
    context = {}
    if request.method == 'POST':
        message = request.POST.get('message')
        chats = request.POST.get('chats')
        chats = chats.split(',')

        API_TOKEN = '7143628618:AAHHyuHEyUePzIouOyrqfcdxmBXP_AD_ZEo'
        bot = telebot.TeleBot(API_TOKEN)

        successful = []
        failed = []
        for chat_id in chats:
            try:
                bot.send_message(chat_id, message)
                successful.append(chat_id)
            except Exception as e:
                failed.append(chat_id)

        context.update({'successful': successful, 'failed': failed})
    return render(request, 'send_message.html', context)
