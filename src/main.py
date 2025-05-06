import flet as ft
import pages as pg

def main(page: ft.Page):

    page.title = "Учет времени"

    # Контейнер для отображения текущей страницы
    content = ft.Container()

    # Функция для обработки смены страницы
    def on_navigation_change(e):
        selected_index = e.control.selected_index
        content.content = None  # Очищаем содержимое
        if selected_index == 0:
            content.content = pg.build_tracker_page()
        elif selected_index == 1:
            content.content = pg.build_interval_page()
        elif selected_index == 2:
            content.content = pg.build_settings_page()
        page.update()


    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.TIMELAPSE_ROUNDED, label="Сейчас"),
            ft.NavigationBarDestination(icon=ft.Icons.HISTORY, label="Рабочие интервалы"),
            ft.NavigationBarDestination(icon=ft.Icons.SETTINGS_APPLICATIONS,label="Настройки"),
        ],
        on_change = on_navigation_change,
        selected_index = 0  # Начальная страница
    )

    # Инициализация начальной страницы
    content.content = pg.build_tracker_page()

    # Добавляем контейнер на страницу
    page.add(content)

ft.app(target=main)