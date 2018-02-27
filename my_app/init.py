from playhouse.db_url import connect
from my_app.configs import MyAppConfig


db = connect(MyAppConfig.MYSQL_DB_URL)
