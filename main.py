import flet as ft
import qrcode
import phototoclipboard
import tempfile


def main(page: ft.Page):
    page.title = "QR Generator"
    page.theme_mode = 'light'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 530
    page.scroll = True


    def createqr(e):
        lastqr = []

        def tempofile(username):

            tempo = tempfile.TemporaryFile(delete=False, suffix='.png', prefix=f"qr-code-{username.value}_")
            lastqr.append(tempo.name)
            print(lastqr[-1])

            # return tempo
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
        qr = qrcode.make(link).save(lastqr[-1])

        page.add(
            ft.Row([
                ft.Container(
                    ft.Image(src=lastqr[-1]),
                    ink=True,
                    on_click=copyqr, alignment=ft.alignment.center)],alignment=ft.alignment.center))

        page.add(ft.Row(
            [
                ft.ElevatedButton('Copy QR', on_click=copyqr),
                ft.IconButton(ft.icons.COPY, on_click=copyurl)
            ]
            ))
        page.update()

    username = ft.TextField(label='UserName', on_submit=createqr,
                            text_align=ft.TextAlign.LEFT, width=320)


    page.add(
        ft.Row(
            [
                username, ft.IconButton(ft.icons.QR_CODE, icon_size=40,
                                        on_click=createqr)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


ft.app(main)
