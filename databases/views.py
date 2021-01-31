from databases.models import Client, Quotes

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView


def index(request):
    return HttpResponse("Index")


class ClientCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Client
    fields = ['first_name', 'last_name', 'product', 'city']
    login_url = '/admin/login/'
    template_name = 'databases/client_form.html'
    success_url = reverse_lazy('client-create')
    success_message = "%(first_name)s was created successfully!"
    redirect_field_name = 'admin'


class ClientUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Client
    fields = ['first_name', 'last_name', 'product', 'city']
    login_url = '/admin/login/'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('client-update')
    success_message = "%(first_name)s was updated successfully!"
    redirect_field_name = 'admin'


class ClientDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    fields = ['first_name', 'last_name', 'product', 'city']
    login_url = '/admin/login/'
    success_url = reverse_lazy('client-list')
    success_message = "%(first_name)s was deleted successfully!"
    redirect_field_name = 'admin' 


class ClientListView(ListView):
    model = Client
    paginate_by = 100


class ClientDetailView(DetailView):
    model = Client
    context_object_name = 'product_details'


class QuotesListView(ListView):
    model = Quotes
    paginate_by = 100

    queryset = Quotes.objects.select_related('author').all()
