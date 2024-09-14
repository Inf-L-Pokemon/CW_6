from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.urls.base import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView

from email_list.forms import ClientForm, MailingMessageForm, MailingSettingsForm
from email_list.models import Client, MailingMessage, MailingSettings


class MainPageView(TemplateView):
    template_name = 'email_list/main_page.html'


class PlugTemplateView(TemplateView):
    template_name = 'email_list/plug.html'


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('email_list:client_list')


class ClientListView(LoginRequiredMixin, ListView):
    model = Client


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm

    def get_success_url(self):
        return reverse('email_list:client_detail', args=[self.kwargs.get('pk')])

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('email_list:client_list')


class MailingMessageCreateView(LoginRequiredMixin, CreateView):
    model = MailingMessage
    form_class = MailingMessageForm
    success_url = reverse_lazy('email_list:mailing_message_create')


class MailingMessageListView(LoginRequiredMixin, ListView):
    model = MailingMessage


class MailingMessageDetailView(LoginRequiredMixin, DetailView):
    model = MailingMessage


class MailingMessageUpdateView(LoginRequiredMixin, UpdateView):
    model = MailingMessage
    form_class = MailingMessageForm

    def get_success_url(self):
        return reverse('email_list:mailing_message_detail', args=[self.kwargs.get('pk')])

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))


class MailingMessageDeleteView(LoginRequiredMixin, DeleteView):
    model = MailingMessage
    success_url = reverse_lazy('email_list:mailing_message_list')


class MailingSettingsCreateView(LoginRequiredMixin, CreateView):
    model = MailingSettings
    form_class = MailingSettingsForm

    def get_success_url(self):
        return reverse('email_list:mailing_settings_detail', args=[self.kwargs.get('pk')])


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
