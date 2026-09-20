# Email send Using SMTP server 
import smtplib
from email.message import EmailMessage

sender = "mdohidul.alam15@gmail.com"
receiver = input("Enter the Receiver Email: ")
receiver_name = input("Enter the Receiver Name: ")
password = "hzbd bewc pkzp drvf"

msg = EmailMessage()
msg["Subject"] = "Happy BirthDay🎉"
msg["From"] = sender
msg["To"] = receiver
msg.set_content(f"Happy Birthday, {receiver_name}! Wishing you a fantastic year ahead! 🎂")

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(sender, password)
    smtp.send_message(msg)

print("Email sent successfully!")