from django.core.management import BaseCommand

from email_list.services import start_scheduler


class Command(BaseCommand):
    """Команда на запуск рассылки"""
    def handle(self, *args, **options):
        start_scheduler()
