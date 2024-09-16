import random

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.urls.base import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView

from blog.models import BlogPost
from email_list.forms import ClientForm, MailingMessageForm, MailingSettingsForm
from email_list.models import Client, MailingMessage, MailingSettings


class MainPageView(TemplateView):
    template_name = 'email_list/main_page.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['count_mailing_settings'] = len(MailingSettings.objects.all())
        context_data['count_active_mailing_settings'] = len(MailingSettings.objects.filter(is_active=True))
        context_data['clients'] = len(Client.objects.all())
        context_data['blog_list'] = random.sample(list(BlogPost.objects.all()), len(list(BlogPost.objects.all())))[:3]

        return context_data


class PlugTemplateView(TemplateView):
    template_name = 'email_list/plug.html'


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('email_list:client_list')

    def form_valid(self, form):
        client = form.save()
        client.owner = self.request.user
        client.save()

        return super().form_valid(form)


class ClientListView(LoginRequiredMixin, ListView):
    model = Client


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm

    def get_success_url(self):
        return reverse('email_list:client_detail', args=[self.kwargs.get('pk')])


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('email_list:client_list')


class MailingMessageCreateView(LoginRequiredMixin, CreateView):
    model = MailingMessage
    form_class = MailingMessageForm
    success_url = reverse_lazy('email_list:mailing_message_list')

    def form_valid(self, form):
        message = form.save()
        message.owner = self.request.user
        message.save()

        return super().form_valid(form)


class MailingMessageListView(LoginRequiredMixin, ListView):
    model = MailingMessage


class MailingMessageDetailView(LoginRequiredMixin, DetailView):
    model = MailingMessage


class MailingMessageUpdateView(LoginRequiredMixin, UpdateView):
    model = MailingMessage
    form_class = MailingMessageForm

    def get_success_url(self):
        return reverse('email_list:mailing_message_detail', args=[self.kwargs.get('pk')])


class MailingMessageDeleteView(LoginRequiredMixin, DeleteView):
    model = MailingMessage
    success_url = reverse_lazy('email_list:mailing_message_list')


class MailingSettingsCreateView(LoginRequiredMixin, CreateView):
    model = MailingSettings
    form_class = MailingSettingsForm
    success_url = reverse_lazy('email_list:mailing_settings_list')

    def form_valid(self, form):
        settings = form.save()
        settings.owner = self.request.user
        settings.save()

        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class MailingSettingsListView(LoginRequiredMixin, ListView):
    model = MailingSettings


class MailingSettingsDetailView(LoginRequiredMixin, DetailView):
    model = MailingSettings


class MailingSettingsUpdateView(LoginRequiredMixin, UpdateView):
    model = MailingSettings
    form_class = MailingSettingsForm

    def get_success_url(self):
        return reverse('email_list:mailing_settings_detail', args=[self.kwargs.get('pk')])


class MailingSettingsDeleteView(LoginRequiredMixin, DeleteView):
    model = MailingSettings
    success_url = reverse_lazy('email_list:mailing_settings_list')
