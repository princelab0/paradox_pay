
from django.contrib.admin.apps import AdminConfig


class CustomAdminConfig(AdminConfig):
    default_site = 'subscription_django.admin.CustomAdminSite'