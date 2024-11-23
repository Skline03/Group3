import smtplib
import sqlite3
from email.message import EmailMessage

# Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "jmiller.scholars@gmail.com"
SENDER_PASSWORD = "akdk kzcb kbfk azve"  # App password

# Database configuration
DATABASE_NAME = "phishing_simulation.db"

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
    subject = "Important: Verify Your Account"
    body = f"""
    Dear User,

    Your account requires verification. Click the link below:

    {tracking_link}

    Thank you,
    IT Security Team
    """
    send_email(recipient_email, subject, body)

def get_clicked_users():
    """
    Retrieves the distinct user IDs from the click log in the database.

    Returns:
        list: A list of user IDs (email addresses) that have clicked the simulated phishing link.
    """
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        c = conn.cursor()
        c.execute("SELECT DISTINCT user_id FROM click_log")
        users = [row[0] for row in c.fetchall()]
        conn.close()
        return users
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []

def send_feedback_email(recipient_email):
    """
    Sends a feedback email to the specified recipient, informing them of their participation
    in a phishing simulation and providing educational content.

    Args:
        recipient_email (str): The email address of the recipient.
    """
    subject = "Phishing Awareness Feedback"
    body = f"""
    Hello,

    You recently clicked on a simulated phishing email. This exercise is designed to raise awareness about phishing attempts. Please review the best practices for identifying phishing emails.

    Stay secure,
    IT Security Team
    """
    send_email(recipient_email, subject, body)

# Main execution
if __name__ == "__main__":
    # Send phishing simulation emails
    phishing_recipients = ["stevenkline27@gmail.com"]  # Replace with actual recipient list
    for recipient in phishing_recipients:
        send_phishing_simulation_email(recipient)

    # Send feedback emails to users who clicked
    clicked_users = get_clicked_users()
    for user in clicked_users:
        send_feedback_email(user)
