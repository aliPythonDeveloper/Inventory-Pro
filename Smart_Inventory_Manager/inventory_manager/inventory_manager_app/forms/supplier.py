from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SupplierModelCreateForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required. Provide a valid email address.")
    company_name = forms.CharField(max_length=255, required=True)
    contact_number = forms.CharField(max_length=15, required=True)
    address = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = False  # Ensure the user is not a staff member or superuser
        user.is_superuser = False
        if commit:
            user.save()
        return user
