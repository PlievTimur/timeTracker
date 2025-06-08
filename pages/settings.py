import flet as ft
import re

from jira_utils import check_jira_connection

def get_content():
    def validate_url(url):
        regex = re.compile(
            r'^(?:http|ftp)s?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain
            r'localhost|'  # localhost
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ip
            r'(?::\d+)?'  # port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        return re.match(regex, url) is not None

    def on_url_submit(e):
        if validate_url(url_input.value):
            url_input.suffix_icon = ft.Icons.CHECK_CIRCLE_OUTLINED
            url_input.border_color = ft.Сolors.GREEN
            print(f"Valid URL: {url_input.value}")
        else:
            url_input.border_color = ft.Сolors.RED
            url_input.suffix_icon=ft.Icons.ERROR_OUTLINE
        url_input.update()


    url_input = ft.TextField(
            label="Введите URL сервера Jira",
            hint_text="https://jira.ursalab.ru/",
            value="https://jira.ursalab.ru/",
            prefix_icon=ft.Icons.LINK,
            suffix_icon=ft.Icons.CHECK_CIRCLE_OUTLINED,
            keyboard_type=ft.KeyboardType.URL,
            border=ft.InputBorder.OUTLINE,
            border_radius=10,
            filled=True,
            on_change=on_url_submit,
            on_submit=on_url_submit,
        )

    def validate_api_key(e):
        api_key = api_key_input.value
        pattern = r'^[a-zA-Z0-9]{12,16}[a-zA-Z0-9]{20,30}$'
        if re.match(pattern, api_key):
            api_key_input.suffix_icon = ft.Icons.CHECK_CIRCLE_OUTLINED
            api_key_input.border_color = ft.Colors.GREEN
            print(ft.Text(f"Валидный API-ключ: {api_key}"))
        else:
            api_key_input.border_color = ft.Сolors.RED
            #api_key_input.suffix_icon=ft.Icons.ERROR_OUTLINE
        api_key_input.update()

    # Поле ввода API-ключа
    api_key_input = ft.TextField(
        label="Введите API-ключ",
        hint_text="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        password=True,  # Скрывает ввод (как пароль)
        can_reveal_password=True,  # Позволяет показать/скрыть ключ
        on_change=validate_api_key,
        on_submit=validate_api_key,
    )

    def test_jira_connect(e):
        check_jira_connection(url_input.value, "pliev@ursalab.ru", api_key_input.value)
        print("ass")

    button_test_connect = ft.ElevatedButton("Проверить подключение", on_click=test_jira_connect)

    page = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="Подключение",
                icon=ft.Icons.LINK ,
                content=ft.Container(
                    content=ft.Column(
                        controls=[url_input,api_key_input,button_test_connect],
                        alignment=ft.alignment.center,
                        spacing=20,
                    ),
                    padding=ft.padding.only(top=20, left=15, right=15)
                )
            ),
            ft.Tab(
                tab_content=ft.Icon(ft.Icons.SEARCH),
                content=ft.Text("This is Tab 2"),
            ),
            ft.Tab(
                text="Tab 3",
                icon=ft.Icons.SETTINGS,
                content=ft.Text("This is Tab 3"),
            ),
        ],
        expand=True,
        #width=400,
        #height=400,
    )

    return page