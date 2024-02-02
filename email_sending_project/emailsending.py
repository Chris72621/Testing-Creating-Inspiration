# currently trying to figure out where this project is heading
import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Set your email and password
sender_email = "projecthelperchris@gmail.com"
sender_password = "ikaq kbsb bdnl opkc"

# Recipient email address
recipient_email = "david71698@yahoo.com"
#graylenleeps24@gmail.com

# Create a MIMEMultipart object
def generate_random_char():
    # Generate a random integer between 1 and 1000
    random_number = random.randint(1, 1000)

    # Convert the random number to a character
    random_char = chr(random_number)
    return random_char

# Send the email
for i in range (40):
    randomChar = generate_random_char()
    message = MIMEMultipart()
    # Set the sender, recipient, and subject
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = "David Sucks" + randomChar

    # Add the email body (text or HTML content)
    body = "Loser"
    message.attach(MIMEText(body, "plain"))

    # Create a connection to the SMTP server (in this case, Gmail)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    # Log in to your email account
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, message.as_string())
print("DONE SENDING")
# Quit the server
server.quit()
