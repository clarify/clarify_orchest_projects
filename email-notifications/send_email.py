import email, smtplib, ssl
import os
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import orchest

data = orchest.get_inputs()["alarm"] # data = (subject, text, maximum, anomaly, plot)

# data[0] = subject -> Everything is fine, no email, no alarm
if data[0] != "": 
    subject = data[0]
    html = data[1]
    plot = data[4]

    sender_email = orchest.get_step_param("sender_email")
    receiver_email = orchest.get_step_param("receiver_email")
    password = os.environ["email-password"]

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Add body to email
    message.attach(MIMEText(html, "html"))

    if plot:
    # Open PDF file in binary mode
        with open("../data/plot.pdf", "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {'plot.pdf'}"
        )

        message.attach(part)
        text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)
    
    message = "Send email 📧"

else: 
    message = "No need to send an email 📧"
    
print(message)
orchest.output((message), name = "message")