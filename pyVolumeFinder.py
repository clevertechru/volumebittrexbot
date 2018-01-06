from bittrex.bittrex import Bittrex, API_V2_0
import time
import bot

initBittrex = Bittrex(None, None)   #Инициализация переменной Bittrex
bitR = initBittrex.get_market_summaries()   #Получение данных о маркете (см. документацию к API Bittrex)
clR = bitR['result']    #Парсинг ответа от Bittrex (оставляем только данные поля result)

def initArray(inputArray):  #функция для обновления массива с показаниями объема
    bitResponse = initBittrex.get_market_summaries()
    clResponse = bitResponse['result']
    for tmpCoin in clResponse:
        inputArray.append(tmpCoin['BaseVolume'])

firstVols = []  #Первый массив для определения начальных показаний объема
secondVols = [] #Второй массив сравниваем с первым и анализируем на сколько прирос объем
curPump = []    #Хранение текущих монет находящихся в пампе
initArray(firstVols)    #получаем первые данные

def finder(fVols):  #функция поиска и отображения монет на пампе (выводит если скачок объема превышает 5%)
    tmpPercent = 0.05
    sVols = []
    initArray(sVols)
    i = 0
    for tmpFVol, tmpSVol in zip(fVols, sVols):
        ifer = tmpSVol/tmpFVol
        if (ifer-1) > tmpPercent:
            cl = clR[i]
            nonExist = True
            for curP in curPump:
                if curP == cl['MarketName']:
                    nonExist = False
            if nonExist:
                bot.send_new_posts(cl, tmpSVol)
                curPump.append(cl['MarketName'])
        i += 1

j = 0
k = 0
while 1:
    finder(firstVols)
    j += 1
    k += 1
    if j > 10:
        firstVols = []
        initArray(firstVols)
        j = 0
        print('Reinit firstVols')
    if k > 20:
        k = 0
        curPump = []
        print('ReInit curPump')
    time.sleep(0.1)
