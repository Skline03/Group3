import smtplib
from email.message import EmailMessage

# Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "jmiller.scholars@gmail.com"  # Your Gmail address
SENDER_PASSWORD = "akdk kzcb kbfk azve"  # Your Gmail app password

def send_email(recipient_email, subject, body):
    """
    Sends an email with the specified subject and body to the recipient.

    Args:
        recipient_email (str): The email address of the recipient.
        subject (str): The subject of the email.
        body (str): The body content of the email.
    """
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg['To'] = recipient_email
    msg.set_content(body)

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
            smtp.starttls()  # Secure the connection
            smtp.login(SENDER_EMAIL, SENDER_PASSWORD)  # Log in to the SMTP server
            smtp.send_message(msg)  # Send the email
            print(f"Email sent successfully to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email to {recipient_email}: {e}")

def send_phishing_simulation_email(recipient_email):
    """
    Sends a phishing simulation email to the specified recipient.

    Args:
        recipient_email (str): The email address of the recipient.
    """
    tracking_link = f"http://127.0.0.1:80/phishing?id={recipient_email}"  # Replace with actual server address
    subject = "Grandma Is sick"
    body = f"""
    Hey Steven,

    your grandmother has gotten sick

    {tracking_link}

    Thank you,
    """
    send_email(recipient_email, subject, body)

# Example usage
if __name__ == "__main__":
    email_list = ["stevenkline27@gmail.com"]  # List of recipients
    for email in email_list:
        send_phishing_simulation_email(email)
