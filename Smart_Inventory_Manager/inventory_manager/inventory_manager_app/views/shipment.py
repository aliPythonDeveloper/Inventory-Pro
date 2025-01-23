from django.views.generic import ListView, DetailView, UpdateView, CreateView, RedirectView, DeleteView, TemplateView
from django.utils.translation import gettext_lazy as _
from ..models import *
from ..forms import *
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin




class ShipmentModelCreateView(LoginRequiredMixin, TemplateView):
    template_name = 'shipment/shipment.html'
    PAGE_TITLE = _("Add shipment Address")
    extra_context = {
        'header_title': PAGE_TITLE,
        'page_title': PAGE_TITLE
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ShipmentModelCreateForm()  # Provide the form for display
        return context
