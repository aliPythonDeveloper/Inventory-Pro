from django.views.generic import RedirectView
from django.urls import reverse
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin





class RootUrlView(LoginRequiredMixin, View):
    template_name = 'layouts/home1.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)