from PIL import ImageGrab
import pytesseract
import webbrowser
import os
import pyautogui
from time import sleep
import win32api
import time

def webopen(url):
    webbrowser.register(
        "chrome",
        None,
        webbrowser.BackgroundBrowser(
            "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        ),
    )
    webbrowser.get("chrome").open(url)
def full():
    im = ImageGrab.grabclipboard()
    im.save(f'{path}\\Pictures\\img.png','PNG')

    pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'
    query = (pytesseract.image_to_string(f"{path}\\Pictures\\img.png"))
    url = "https://google.com/search?query=" + query
    webopen(url)

path = (os.path.expanduser('~'))

pyautogui.hotkey("win", "shift", "s")

state_left = win32api.GetKeyState(0x01)
state_right = win32api.GetKeyState(0x02)

while True:
    a = win32api.GetKeyState(0x01)
    b = win32api.GetKeyState(0x02)

    if a != state_left:
        state_left = a
        if a < 0:
            pass
        else:
            sleep(1)
            full()
            break
