import config
import telebot  #Используются API телеграма

bot = telebot.TeleBot(config.token)

#Необходимо создать канал и добавить в него администратором бота (токен бота в config.py)
CHANNEL_NAME = '@volbittrex'

def toFixed(f, n=0):    #функция для оставления двух знаков после запятой для типа float
    a, b = str(f).split('.')
    return '{}.{}{}'.format(a, b[:n], '0'*(n-len(b)))

def send_new_posts(mes, tmpSVol): #Функция отправки в канал
    increaser = 100.*(tmpSVol/mes['BaseVolume'] - 1)
    message = 'Bittrex ' + mes['MarketName'] + ' Increase volume: ' + str(toFixed(increaser, 2)) + '%'
    bot.send_message(CHANNEL_NAME, message)
    return

if __name__ == '__main__':
     bot.polling(none_stop=True)
