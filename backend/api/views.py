# api/views.py
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import EmailSerializer
from django.conf import settings

@api_view(['POST'])
def send_email_view(request):
    serializer = EmailSerializer(data=request.data)
    if serializer.is_valid():
        data = serializer.validated_data

        # Email details
        subject = f"Thank you, {data['name']}!"
        # Base message
        message = (
            f"Hello {data['name']},\n\n"
            f"Thank you for reaching out. We have received your message:\n\n"
            f"'{data['message']}'\n\n"
            f"We will get back to you soon.\n\n"
        )
        # Additional message if subscribed to the newsletter
        if data['subscribeNewsletter']:
            message += (
                "Additionally, thank you for subscribing to our newsletter! "
                "You'll receive updates and news directly to your inbox.\n\n"
            )
        # Closing message
        message += "Best Regards,\nThe Team"

        recipient_email = data['email']  # Send to the user's email from the form
        sender_email = settings.EMAIL_HOST_USER  # Use the configured host email

        try:
            # Send email
            send_mail(subject, message, sender_email, [recipient_email])
            return Response({"message": "Email sent successfully!"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": "Failed to send email"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
