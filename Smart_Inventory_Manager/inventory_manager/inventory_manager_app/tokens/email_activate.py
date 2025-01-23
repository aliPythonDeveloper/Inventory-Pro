from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from .tokens import email_verification_token

def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and email_verification_token.check_token(user, token):
        user.is_active= True
        user.save()
        print("USER IS ACTIVATED")
        messages.success(request, "thank you for your email configuration. Now you can login your account")
        return redirect("inventory_manager_app:login")
    else:
        messages.error(request, "Activation link is invalid!")

    return redirect('inventory_manager_app:home')

def activateEmail(request, user, to_email):
    mail_subject = "Activate your account"
    message = render_to_string("email/template_activate_account.html", {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': email_verification_token.make_token(user),
        'protocol': 'https' if request.is_secure() else "http"
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.info(request, f'Dear <b>{user}</b>, please go to your email <b>{to_email}</b> inbox and click on \
                                  received activation link to confirm and complete the registration, <b>Note: </b> Check your spam folder.')
    else:
        messages.error(request, f'Problem sending email to {to_email}, check if you type if correctly.')
