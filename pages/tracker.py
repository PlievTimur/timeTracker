import flet as ft


def get_content():
    return ft.Column([
        ft.Text("Страница 'Сейчас'", size=20),
        ft.ElevatedButton("Тест", on_click=lambda e: print("Тестовая кнопка на странице 'Сейчас'"))
    ])
