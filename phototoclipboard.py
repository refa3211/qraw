from io import BytesIO
import win32clipboard
from PIL import Image


def send_to_clipboard(clip_type, data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()


def getphoto(photopath):
    image = Image.open(photopath)
    output = BytesIO()
    image.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    print(data)
    output.close()
    send_to_clipboard(win32clipboard.CF_DIB, data)

# getphoto('images\qr-.png')
