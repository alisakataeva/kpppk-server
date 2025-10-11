import smtplib
from email.message import EmailMessage


#


def get_feedback_from_landing_page():
    pass


def send_feedback_email():
    msg = EmailMessage()
    msg.set_content('This is the body of the email.')
    msg['Subject'] = 'My Subject Line'
    msg['From'] = 'sweetqiwi@gmail.com'
    msg['To'] = 'alisakataeva999@gmail.com'

    try:
        # For Gmail, use 'smtp.gmail.com' and port 587 with starttls() for security
        # For other providers, consult their documentation for server and port
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Secure the connection
            server.login('sweetqiwi@gmail.com', 'kgjz aekr wvmo fcqg ') # Use an app password for Gmail
            server.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")
