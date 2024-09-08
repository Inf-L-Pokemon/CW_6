from datetime import datetime

from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    email = models.EmailField(unique=True, verbose_name='Почта')
    first_name = models.CharField(max_length=20, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=30, verbose_name='Отчество', **NULLABLE)
    description = models.TextField(verbose_name='Комментарий', **NULLABLE)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                              verbose_name='Владелец карточки клиента', **NULLABLE)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.patronymic} ({self.email})'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class MailingMessage(models.Model):
    subject = models.CharField(max_length=100, verbose_name='Тема письма')
    message = models.TextField(verbose_name='Сообщение', **NULLABLE)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                              verbose_name='Владелец сообщения для рассылки', **NULLABLE)

    def __str__(self):
        return f'{self.subject}: {self.message}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class MailingSettings(models.Model):
    periods = (('per_day', 'раз в день'), ('per_week', 'раз в неделю'), ('per_month', 'раз в месяц'))
    statuses = (('created', 'создана'), ('started', 'запущена'), ('completed', 'завершена'))

    start_datetime = models.DateTimeField(default=datetime.now, verbose_name='Начало рассылки')
    end_datetime = models.DateTimeField(default=datetime.now, verbose_name='Окончание рассылки')

    period = models.CharField(max_length=15, choices=periods, default='per_month', verbose_name='Период рассылки')
    status = models.CharField(max_length=15, choices=statuses, default='created', verbose_name='Статус рассылки')
    is_active = models.BooleanField(default=False, verbose_name='Активна')

    clients = models.ManyToManyField(Client, verbose_name='Получатели')
    mail_message = models.ForeignKey(MailingMessage, on_delete=models.CASCADE, verbose_name='Сообщение', **NULLABLE)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                              verbose_name='Владелец рассылки', **NULLABLE)

    def __str__(self):
        return f'{self.mail_message.subject}. {self.status}. {'Активна' if self.is_active else 'Не активна'}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class Attempt(models.Model):
    statuses = ((True, 'Успешно'), (False, 'Не успешно'))

    last_attempt_datetime = models.DateTimeField(auto_now=True, verbose_name='Дата и время последней попытки рассылки',
                                                 **NULLABLE)
    status = models.CharField(max_length=10, choices=statuses, default=True, verbose_name='Статус попытки', **NULLABLE)

    mailing_settings = models.ForeignKey(MailingSettings, on_delete=models.CASCADE, verbose_name='Рассылка', **NULLABLE)

    def __str__(self):
        return f'{self.mailing_settings.mail_message.subject}. {self.last_attempt_datetime} - {self.status}.'

    class Meta:
        verbose_name = 'Попытка рассылки'
        verbose_name_plural = 'Попытки рассылки'
