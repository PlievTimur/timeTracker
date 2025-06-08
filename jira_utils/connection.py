import logging

from jira import JIRA


def check_jira_connection(jira_url: str, email: str, api_key: str) -> bool:
    try:
        jira = JIRA(
            server=jira_url,
            basic_auth=(email, api_key),
            options={"verify": False}
        )

        projects = jira.projects()
        print(projects)
    except Exception as e:
        logging.error(f"Ошибка подключения к Jira: {e}")
        return False
