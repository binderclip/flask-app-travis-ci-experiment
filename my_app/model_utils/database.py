import pymysql
from my_app.configs import MyAppConfig


conn = pymysql.connect(
    host=MyAppConfig.MYSQL_HOST,
    user=MyAppConfig.MYSQL_USER,
    password=MyAppConfig.MYSQL_PASSWORD)


def create_database():
    conn.cursor().execute(
        f'CREATE DATABASE IF NOT EXISTS {MyAppConfig.MYSQL_DB_NAME} '
        'DEFAULT CHARACTER SET utf8mb4 '
        'DEFAULT COLLATE utf8mb4_unicode_ci;',
    )


def drop_database():
    conn.cursor().execute(f'DROP DATABASE IF EXISTS {MyAppConfig.MYSQL_DB_NAME};')
