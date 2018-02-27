# coding: utf-8
import os

__all__ = ['MyAppConfig']

app_config_file_name = os.environ.get('MY_APP_CONFIG', '')
if not app_config_file_name:
    raise Exception('No MY_APP_CONFIG in os environ, should be something like: xxx_config')
app_config_module = __import__('my_app.configs.{}'.format(app_config_file_name), fromlist=['Config'])

MyAppConfig = app_config_module.Config
