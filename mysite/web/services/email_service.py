import mimetypes

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings




def send_customer_confirmation(quote):
    
    subject = "Confirmation of your quote request"
    
    html_content = render_to_string("emails/customer_confirmation.html", {"quote": quote})
    
    email = EmailMultiAlternatives(
        subject=subject,
        body="Thank you for requesting a quote",
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[quote.email],
    )
    
    email.attach_alternative(html_content, "text/html")
    email.send()
    
def send_admin_notification(quote):
    subject = f"New Quote Request - {quote.full_name}"
    
    html_content = render_to_string(
        "emails/admin_notification.html",
        {"quote": quote},
    )
    
    email = EmailMultiAlternatives(
        subject=subject,
        body="A new quote request has been submited.",
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[settings.ADMIN_EMAIL],
        reply_to=[quote.email],
    )
    email.attach_alternative(html_content, "text/html")
    
    # Attach uploaded photos
    for photo in quote.quote_photos.all():
        if photo.image:
            mime_type, _ = mimetypes.guess_type(photo.image.path)

            with open(photo.image.path, "rb") as f:
                email.attach(
                    filename=photo.image.name.split("/")[-1],
                    content=f.read(),
                    mimetype=mime_type or "application/octet-stream",
                )
        
    email.send()
    
    