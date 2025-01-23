from django.views.generic import CreateView
from ..forms import WholeSalerModelCreateForm
from django.urls import reverse
from ..models import wholeSaler
from django.contrib.auth.models import  Group
from django.contrib.auth.models import User
from ..tokens.email_activate import *
from django.contrib.auth.mixins import LoginRequiredMixin


class WholesalerRegisterView(CreateView):
    model = User
    form_class = WholeSalerModelCreateForm
    template_name = 'wholesaler/wholesaler_auth.html'

    def form_valid(self, form):
        # Create the user
        user = form.save(commit=False)
        user.is_active=False
        user.save()
        activateEmail(self.request, user, form.cleaned_data.get('email'))

        # Assign the user to the 'Supplier' group
        wholesaler_group, _ = Group.objects.get_or_create(name='Wholesaler')
        user.groups.add(wholesaler_group)

        # Create a related Supplier instance
        wholeSaler.objects.create(
            user=user,
            company_name=form.cleaned_data['company_name'],
            contact_number=form.cleaned_data['contact_number'],
            address=form.cleaned_data['address']
        )

        return super().form_valid(form)
        # return redirect("inventory_manager_app:home")

    def get_success_url(self):
        return reverse('inventory_manager_app:login')


