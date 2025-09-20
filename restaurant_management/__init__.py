from django.core.mail import send_mail, BadHeaderError
from django .conf import settings import logging
logger = logging.getLogger(__name__)
def send_order_confirmation_email(order_id, custmoer_email):
   subject = f"Order Confirmation - #{order_id}"
   message = (
    f"Dear Customer,\n\"
    f"Thank  you for your purchase!\n"
    f"Your will notify you once ID{order_id} has been successfully placed.\n\n"
    f"We will notify you once your itmes are shipped.\n\"
    f"Best regards,\nYour Shop Team"
    )
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [customer_email]
    try:
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        logger.info(f"Order confirmation email sent to {customer_email} for Order ID {order_id}")
        return True
    except BadHeaderError:
        logger.error("Invalid header found while sending email.")
        return False
    except Exception as e:
        logger.error(f"Error sending order confirmation email:{str(e)}")
        return False
        EMAIL_BACKEND = 'django.core.mail.backend.smtp,EmailBackend'
        EMAIL_HOST = 'smpt.gmail.com'
        EMAIL_PORT = 587
        EMAIL_USE_TLS = True
        EMAIL_HOST_USER = 'your_email@gmail.com'
        EMAIL_HOST_PASSWORD = 'your_app_password'
        DEFAULT_FROM_EAMIL= EMAIL_HOST_USER
        from utils import
        send_order_confirmation_email
        from django.http import JsonResponse
        def place_order*=(request):
            order_id = 14246
            customer_email = "customer@example.com"
            email_status = send_order_confirmation_email(order_id, customer_email)
            if email_status:
                return JosnResponse({"message": "Order placed and confirmation email sent."})
                else:
                    return JosnResponse({"message": "Order placed but email failed to send."}, status=500)
