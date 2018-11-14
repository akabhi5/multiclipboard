from threading import *
import pyperclip

data = ''
oldtext = ''

gettext = pyperclip.paste()
randtxt = gettext

def readData():
    global oldtext
    with open('clipboardcontent.txt', 'r') as f:
        data = f.read()
    # print(data)
    # print(len(data))
    return data

def fun():
    while True:
        global randtxt, gettext, oldtext
        try:
            f = open('clipboardcontent.txt', 'a')
        except:
            pass

        gettext = pyperclip.paste()

        if randtxt != gettext:
            if oldtext != gettext:
                # print(gettext)
                f.write(str(gettext) + '\n' + '------------\n')
                oldtext = gettext

        f.close()


'''daemon thread will stop when main thread stops'''

def startthread():

    th1 = Thread(target=fun)
    th1.setDaemon(True)

    th2 = Thread(target=readData)
    th2.setDaemon(True)

    th1.start()
    th2.start()

def deletedata():
    try:
        f = open('clipboardcontent.txt', 'w')
    except:
        pass
    finally:
        f.close()