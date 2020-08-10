from PIL import ImageGrab
import time
import pyautogui


def hit(key):
    pyautogui.keyDown(key)


def drawRectangle(data):
    for i in range(400, 580):
        for j in range(600, 720):
            if data[i, j] >= 80:
                hit('up')
                pyautogui.keyUp('up')
                return True
    for i in range(400, 580):
        for j in range(500, 580):
            if data[i, j] >= 80:
                hit('down')
                pyautogui.keyUp('down')
                return True
    return False


if __name__ == '__main__':
    time.sleep(3)
    hit('space')
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        drawRectangle(data)
        '''
        for i in range(380, 450):
            for j in range(600, 720):
                data[i, j] = 0
        for i in range(380, 450):
            for j in range(500, 580):
                data[i, j] = 0

        image.show()
        break
        '''