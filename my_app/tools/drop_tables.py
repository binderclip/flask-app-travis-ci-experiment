import os
from my_app.model_utils.table import drop_tables


def main():
    app_config_file_name = os.environ.get('MY_APP_CONFIG', '')
    if not app_config_file_name or (
            'dev' not in app_config_file_name and
            'test' not in app_config_file_name):
        print('no dev or test in MY_APP_CONFIG, exit')
        return
    drop_tables()
    print('=== drop tables done ===')


if __name__ == '__main__':
    main()
