import smtplib

YOUR_GOOGLE_EMAIL = 'jmiller.scholars@gmail.com'  # The email you setup to send the email using app password
YOUR_GOOGLE_EMAIL_APP_PASSWORD = 'akdk kzcb kbfk azve'  # The app password you generated

smtpserver = smtplib.SMTP_SSL('smtp.gmail.com', 465)
smtpserver.ehlo()
smtpserver.login(YOUR_GOOGLE_EMAIL, YOUR_GOOGLE_EMAIL_APP_PASSWORD)

# Test send mail
sent_from = YOUR_GOOGLE_EMAIL
sent_to = sent_from  #  Send it to self (as test)
email_text = 'This is a test'
smtpserver.sendmail(sent_from, sent_to, email_text)

# Close the connection
smtpserver.close()