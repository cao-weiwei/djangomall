from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AccountsConfig(AppConfig):
    name = 'accounts'
    # 指定应用可读名称
    verbose_name = _('Accounts')
