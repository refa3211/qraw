# import modules
import qrcode
from PIL import Image
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import io

app = FastAPI()


@app.get("/qr")
def qrlogo(username: str = None, ico='logo.png'):
    if username is None:
        return "Enter username"
        
    # taking image which user wants
    logo = Image.open(ico)

    # taking base width
    basewidth = 100

    # adjust image size
    wpercent = (basewidth / float(logo.size[0]))
    hsize = int((float(logo.size[1]) * float(wpercent)))
    logo = logo.resize((basewidth, hsize), Image.LANCZOS)
    QRcode = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    # taking url or text
    url = f'https://getwsone.com/?serverurl=mohconsole.health.gov.il&gid=MOH&un={username}'

    # adding URL or text to QRcode
    QRcode.add_data(url)

    # generating QR code
    QRcode.make(fit=True)

    # taking color name from user
    QRcolor = 'BLACK'

    # adding color to QR code
    QRimg = QRcode.make_image(
        fill_color=QRcolor, back_color="white").convert('RGB')

    # set size of QR code
    pos = ((QRimg.size[0] - logo.size[0]) // 2,
           (QRimg.size[1] - logo.size[1]) // 2)
    QRimg.paste(logo, pos)

    buffer = io.BytesIO()

    # save the QR code generated
    QRimg.save(buffer, "PNG")
    buffer.seek(0)

    return StreamingResponse(io.BytesIO(buffer.read()), media_type="image/png")


