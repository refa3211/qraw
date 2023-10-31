import flet as ft
import qrcode
import phototoclipboard
import tempfile
import qrlogo


def main(page: ft.Page):
    page.title = "QR Generator"
    page.theme_mode = 'light'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 500
    page.window_height = 770
    page.scroll = True

    page.update()

    def createqr(e):
        lastqr = []

        def tempofile(username):
            tempo = tempfile.TemporaryFile(delete=False, suffix='.png',
                                           prefix=f"qr-code-{username.value}_")
            lastqr.append(tempo.name)

        tempofile(username=username)

        def copyurl(e):
            page.snack_bar = ft.SnackBar(ft.Text("copied URL",
                                                 text_align=ft.TextAlign.CENTER))
            page.snack_bar.open = True
            page.snack_bar.duration = 2000
            page.set_clipboard(link)
            page.update()

        def copyqr(e):
            phototoclipboard.getphoto(lastqr[-1])
            page.snack_bar = ft.SnackBar(ft.Text("copied QR code",
                                                 text_align=ft.TextAlign.CENTER))
            page.snack_bar.open = True
            page.snack_bar.duration = 2000
            page.update()

        link: str = f"https://getwsone.com/?serverurl=mohconsole.health.gov.il&gid=MOH&un={username.value}"
        # qr = qrcode.make(link).save(lastqr[-1])
        qrlogo.qrlogo(username=username.value, savefile=lastqr[-1])

        qrimage = ft.Container(content=ft.Image(src=lastqr[-1]),
                               ink=True,
                               height=450,
                               width=450,
                               on_click=copyqr,
                               padding=5,
                               )
        textusername = ft.Text(f"username: {username.value}", size=25)
        copybtnqr = ft.ElevatedButton('Copy QR', on_click=copyqr)
        icnbtn = ft.IconButton(ft.icons.COPY, on_click=copyurl)

        page.add(ft.Row([textusername], alignment=ft.MainAxisAlignment.CENTER),
                 ft.Row([qrimage], alignment=ft.MainAxisAlignment.CENTER),
                 ft.Row([icnbtn, copybtnqr])
                 )

    def getdata():
        username = ft.TextField(label='UserName', on_submit=createqr,
                                text_align=ft.TextAlign.LEFT, width=320)
        qricon = ft.IconButton(ft.icons.QR_CODE, icon_size=40,
                               on_click=createqr)

        page.add(ft.Row([username, qricon],
                        alignment=ft.MainAxisAlignment.CENTER))

        # page.clean()
        page.update()

        return username

    page.update()

    username = getdata()
    # page.views.clear()
    # page.update()


ft.app(main)
