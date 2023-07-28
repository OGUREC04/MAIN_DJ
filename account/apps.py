from django.apps import AppConfig
from django.apps import AppConfig


class ArticlesConfig(AppConfig):
    # default_auto_field = 'django.db.models.BigAutoField'
    name = 'account'
    verbose_name = 'acc'


# class UsersConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'account'
#
#     def ready(self):
#         import account.signals
