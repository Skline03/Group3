import smtplib
from email.message import EmailMessage


def send_email(recipient_email):
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    SENDER_EMAIL = "jmiller.scholars@gmail.com"  # Gmail address
    SENDER_PASSWORD = "akdk kzcb kbfk azve"  # Gmail app password
#----------------------------------------------------------------------------------------------------------------------------------------------
    # Create the email message
    msg = EmailMessage()
    msg['Subject'] = "Scholarship Information"
    msg['From'] = SENDER_EMAIL  # Corrected variable name
    msg['To'] = recipient_email

    # HTML for the email
    html_content = """
    <html>
        <body>
            <p>Dear Sir/Ma'am,</p>
            <p>You are receiving this information because there are potential scholarships and/or financial reimbursements available to you based on criteria you have recently met.
            Please follow the link below to view the relevant scholarship information:</p>
            <p>
                <a href="https://2ly.link/21JVG" style="color: blue;">Scholar Information</a>
            </p>
            <p>These opportunities are limited in capacity, so please act quickly.</p>
            <p><strong>Thank you for your prompt attention to this matter.</strong></p>
            <p><strong>Best regards,<br>Jason Miller</strong></p>
        </body>
    </html>
    """
    # Set the content type to HTML
    msg.add_alternative(html_content, subtype='html')
#---------------------------------------------------------------------------------------------------------------------
    try:
        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
            smtp.starttls()  # Upgrade the connection to secure
            smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
            smtp.send_message(msg)
            print(f"Email sent to {recipient_email}")
    except smtplib.SMTPAuthenticationError:
        print("Authentication failed. Please check your credentials.")
    except smtplib.SMTPException as e:
        print(f"SMTP error occurred: {e}")
    except Exception as e:
        print(f"Failed to send email: {e}")
#----------------------------------------------------------------------------------------------------------------------
email_list = ["kylinhertz7@gmail.com", "stevenkline27@gmail.com",
"froggetier@gmail.com",
"josip.kline@outlook.com",
"esk525@gmail.com",
"officialjohnsmithreal@gmail.com",
"rbigreesejr@gmail.com",
"adriancaronna@gmail.com",
"throwawayhirsch@gmail.com",
"YaynaraPeralta4@gmail.com",
"sofiadakota@icloud.com",
"michaelwallen0704@gmail.com",
"isama1213@gmail.com"]
for email in email_list:
    send_email(email)
