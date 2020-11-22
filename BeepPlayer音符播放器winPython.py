import winsound
inputword = input("输入简谱两个八度高八度加‘+’,如高八度C:'+1',两音中间不空格 <<<")
word=inputword    #简谱
lenword=0

while lenword < len(word):
    #判断剩余音符数量
    #我也不知道为啥这样可以跑起来
    if word[lenword]==str(1):
        winsound.Beep(262,250)
    elif word[lenword]==str(2):
        winsound.Beep(294,250)
    elif word[lenword]==str(3):
        winsound.Beep(330,250)
    elif word[lenword]==str(4):
        winsound.Beep(349,250)
    elif word[lenword]==str(5):
        winsound.Beep(392,250)
    elif word[lenword]==str(6):
        winsound.Beep(440,250)
    elif word[lenword]==str(7):
        winsound.Beep(494,250)
    elif word[lenword]==str(0):
        time.sleep(0.5)
    elif word[lenword] == str("+") and word[lenword+1] == str("1"):
        winsound.Beep(523,250)
        lenword=lenword+1
    elif word[lenword] == str("+") and word[lenword+1] == str("2"):
        winsound.Beep(587,250)
        lenword=lenword+1
    elif word[lenword] == str("+") and word[lenword+1] == str("3"):
        winsound.Beep(659,250)
        lenword=lenword+1
    elif word[lenword] == str("+") and word[lenword+1] == str("4"):
        winsound.Beep(698,250)
        lenword=lenword+1
    elif word[lenword] == str("+") and word[lenword+1] == str("5"):
        winsound.Beep(784,250)
        lenword=lenword+1
    elif word[lenword] == str("+") and word[lenword+1] == str("6"):
        winsound.Beep(880,250)
        lenword=lenword+1
    elif word[lenword] == str("+") and word[lenword+1] == str("7"):
        winsound.Beep(988,250)
        lenword=lenword+1

    lenword += 1
