

class Config(object):

    MYSQL_USER = "root"
    MYSQL_PASSWORD = ""
    MYSQL_HOST = "localhost"
    MYSQL_PORT = 3306
    MYSQL_DB_NAME = "testdb"
    MYSQL_DB_URL = "mysql://{user}:{password}@{host}:{port}/{db_name}?charset=utf8mb4".format(
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        host=MYSQL_HOST,
        port=MYSQL_PORT,
        db_name=MYSQL_DB_NAME,
    )
