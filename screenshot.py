import time
import pyautogui

def screenshot():
    image_name = int(round(time.time() * 1000))
    image_name = "{}.png".format(image_name)
    time.sleep(5)
    img = pyautogui.screenshot(image_name)
    img.show()

screenshot()