from django.views.generic import CreateView
from ..forms import SupplierModelCreateForm
from django.urls import reverse
from ..models import Supplier
from django.contrib.auth.models import  Group
from django.contrib.auth.models import User
from ..tokens.email_activate import *
from django.contrib.auth.mixins import LoginRequiredMixin



class SupplierRegisterView(CreateView):
    model = User
    form_class = SupplierModelCreateForm
    # template_name = 'supplier/supplier_register.html'
    template_name = 'supplier/supplier_auth.html'

    def form_valid(self, form):
        # Create the user
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        activateEmail(self.request, user, form.cleaned_data.get('email'))

        # Assign the user to the 'Supplier' group
        supplier_group, _ = Group.objects.get_or_create(name='Supplier')
        user.groups.add(supplier_group)

        # Create a related Supplier instance
        Supplier.objects.create(
            user=user,
            company_name=form.cleaned_data['company_name'],
            contact_number=form.cleaned_data['contact_number'],
            address=form.cleaned_data['address']
        )

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('inventory_manager_app:home')


