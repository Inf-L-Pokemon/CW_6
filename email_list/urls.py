from django.urls import path

from email_list.apps import EmailListConfig
from email_list.views import ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, ClientDeleteView, \
    PlugTemplateView, MailingMessageCreateView, MailingMessageListView, MailingMessageDetailView, \
    MailingMessageUpdateView, MailingMessageDeleteView

app_name = EmailListConfig.name

urlpatterns = [
    path('client/create/', ClientCreateView.as_view(), name='client_create'),
    path('client/list', ClientListView.as_view(), name='client_list'),
    path('client/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('client/update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('client/delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),
    path('mailingmessage/create/', MailingMessageCreateView.as_view(), name='mailing_message_create'),
    path('mailingmessage/list', MailingMessageListView.as_view(), name='mailing_message_list'),
    path('mailingmessage/<int:pk>/', MailingMessageDetailView.as_view(), name='mailing_message_detail'),
    path('mailingmessage/update/<int:pk>/', MailingMessageUpdateView.as_view(), name='mailing_message_update'),
    path('mailingmessage/delete/<int:pk>/', MailingMessageDeleteView.as_view(), name='mailing_message_delete'),
    path('plug/', PlugTemplateView.as_view(), name='plug'),
]
