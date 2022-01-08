from PIL import ImageGrab
import pytesseract
import webbrowser
import os
path = (os.path.expanduser('~'))

def webopen(url):
    webbrowser.register(
        "chrome",
        None,
        webbrowser.BackgroundBrowser(
            "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        ),
    )
    webbrowser.get("chrome").open(url)


im = ImageGrab.grabclipboard()
im.save(f'{path}\\Pictures\\img.png','PNG')

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'
query = (pytesseract.image_to_string(f"{path}\\Pictures\\img.png"))
url = "https://google.com/search?query=" + query
webopen(url)
