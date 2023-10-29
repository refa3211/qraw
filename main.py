import flet as ft
import qrcode
import win32clipboard


def main(page: ft.Page):
    page.title = "QR Generator"
    page.theme_mode = 'light'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 550
    page.scroll = True

    def createqr(e):
        def copyurl(e):
            page.snack_bar = ft.SnackBar(ft.Text("copied URL",
                                                 text_align=ft.TextAlign.CENTER))
            print("copied")
            page.snack_bar.open = True
            page.snack_bar.duration = 2000
            page.set_clipboard(link)
            page.update()

        def copyqr(e):
            page.snack_bar = ft.SnackBar(ft.Text("copied QR code",
                                                 text_align=ft.TextAlign.CENTER))
            page.snack_bar.open = True
            page.snack_bar.duration = 2000
            page.update()
            page.set_clipboard(f"./images/qr-{username.value}.png")

            page.update()

        link: str = f"https://getwsone.com/?serverurl=mohconsole.health.gov.il&gid=MOH&un={username.value}"

        qr = qrcode.make(link).save(f"./images/qr-{username.value}.png")

        page.add(
            ft.Row([
                ft.Container(
                    ft.Image(src=f"./images/qr-{username.value}.png"),
                    ink=True,
                    on_click=copyqr,
                    bgcolor=ft.colors.LIGHT_BLUE

                )
            ]
            )

        )

        page.add(
            ft.Row([
                ft.Container(
                    content=ft.Text(link, color=ft.colors.BLUE),
                    on_click=copyurl,
                    ink=True
                )]))

        page.add(ft.ElevatedButton('Copy QR', on_click=copyqr),
                 ft.IconButton(ft.icons.COPY, on_click=copyurl))
        page.update()

    username = ft.TextField(label='UserName', on_submit=createqr,
                            text_align=ft.TextAlign.LEFT, width=280)

    page.add(
        ft.Row(
            [
                username, ft.IconButton(ft.icons.QR_CODE, icon_size=35,
                                        on_click=createqr)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


ft.app(main)
