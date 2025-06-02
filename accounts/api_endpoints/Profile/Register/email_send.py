from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings

def send_register_confirm_email(email, token):
    subject = "Confirm your registration"
    to_email = email
    context = {
        "token": token,
        "frontend_url": "Theboringmmerce.com",
    }
    html_content = render_to_string("rconfirm_register_email.html", context)
    email = EmailMessage(subject, html_content, to=[to_email])
    email.content_subtype = "html"
    email.send()
