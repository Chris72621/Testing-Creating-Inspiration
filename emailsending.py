# currently trying to figure out where this project is heading

import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Set your email and password
sender_email = ""
sender_password = "ikaq kbsb bdnl opkc"

# Recipient email address
recipient_email = ""
#graylenleeps24@gmail.com

# Create a MIMEMultipart object
def generate_random_char():
    # Generate a random integer representing ASCII value of a character
    random_ascii = random.randint(ord('a'), ord('z'))

    # Convert the ASCII value to a character
    random_char = chr(random_ascii)

    return random_char

# Send the email
for i in range (1000):
    randomChar = generate_random_char()
    message = MIMEMultipart()
    # Set the sender, recipient, and subject
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = "I SEE YOU " + randomChar

    # Add the email body (text or HTML content)
    body = "This is the body of the email. Should be three emails"
    message.attach(MIMEText(body, "plain"))

    # Create a connection to the SMTP server (in this case, Gmail)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    # Log in to your email account
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, message.as_string())

# Quit the server
server.quit()
