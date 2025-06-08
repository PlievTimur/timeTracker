import flet as ft
import pages.tracker as traker_page
import pages.intervals as intervals_page
import pages.settings as settings_page
from lang.Translator import Translator


def main(page: ft.Page):

    txt = Translator("en")

    page.title = txt.translate("main_page_title")

    container = ft.Container()

    def on_navigation_change(e):
        selected_index = e.control.selected_index
        container.content = None
        if selected_index == 0:
            container.content = traker_page.get_content()
        elif selected_index == 1:
            container.content = intervals_page.get_content()
        elif selected_index == 2:
            container.content = settings_page.get_content()
        page.update()


    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.TIMELAPSE_ROUNDED, label="Сейчас"),
            ft.NavigationBarDestination(icon=ft.Icons.HISTORY, label="Рабочие интервалы"),
            ft.NavigationBarDestination(icon=ft.Icons.SETTINGS_APPLICATIONS,label="Настройки"),
        ],
        on_change = on_navigation_change,
        selected_index = 0  # default page
    )

    # Инициализация начальной страницы
    container.content = traker_page.get_content()

    # Добавляем контейнер на страницу
    page.add(container)

ft.app(target=main)