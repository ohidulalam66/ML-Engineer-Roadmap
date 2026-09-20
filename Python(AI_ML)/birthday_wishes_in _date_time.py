# Email send using SMTP server
import os
import smtplib
import time
from email.message import EmailMessage
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# Sender's Gmail address and App Pasword here
sender = os.getenv("SMTP_EMAIL")
password = os.getenv("SMTP_PASSWORD")

# Get receiver information
receiver = input("Enter the Receiver's Email: ")
receiver_name = input("Enter the Receiver's Name: ")
receiver_dob = input("Enter the Receiver's DOB (dd-mm): ")



# Birthday time
receiver_time_hour = 21
receiver_time_minute = 10


while True:

    # Get current date and time
    now = datetime.now()

    # Convert today's date to dd-mm format
    today = now.strftime("%d-%m")

    # Check birthday date and time
    if (
        receiver_dob == today
        and now.hour == receiver_time_hour
        and now.minute == receiver_time_minute
    ):

        # Create email
        msg = EmailMessage()

        # Email subject
        msg["Subject"] = "Happy Birthday 🎉"

        # Sender
        msg["From"] = sender

        # Receiver
        msg["To"] = receiver

        # Email body
        msg.set_content(
            f"Happy Birthday, {receiver_name}! "
            "Wishing you a fantastic year ahead! 🎂"
        )

        try:

            # Connect to Gmail SMTP server
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:

                # Login to Gmail
                server.login(sender, password)

                # Send email
                server.send_message(msg)

            print("Birthday wishes sent successfully!")

            # Stop after sending
            break

        except Exception as e:

            print("Failed to send wishes:", e)

    else:

        # Birthday time has not arrived yet
        print(
            f"Waiting... Current time: "
            f"{now.strftime('%d-%m %H:%M:%S')}"
        )

    # Check again after 30 seconds
    time.sleep(30)