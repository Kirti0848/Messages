#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import smtplib
import pywhatkit
from twilio.rest import Client

# Function to send a WhatsApp message using PyWhatKit
def send_whatsapp_message():
    phone_number = input("Enter the recipient's phone number with country code: ")
    message = input("Enter the WhatsApp message: ")
    pywhatkit.sendwhatmsg(phone_number, message, 00, 9)  # Send WhatsApp message

# Function to send an email using SMTP
def send_email():
    sender_email = "testmail@gmail.com"
    sender_password =  "jh jh jg lj nj"
    recipient_email = input("enter the recipient mail")
    subject = input("Enter the email subject: ")
    message = input("Enter the email message: ")

    try:
        # Create an SMTP server object for your email provider (e.g., Gmail)
        smtp_server = smtplib.SMTP("smtp.gmail.com", 587)

        # Start a TLS (Transport Layer Security) connection
        smtp_server.starttls()

        # Login to your email account
        smtp_server.login("testmail@gmail.com", "jeed enfr fdfg resf" )

        # Compose the email
        email_message = f"Subject: {subject}\n\n{message}"

        # Send the email
        smtp_server.sendmail(sender_email, recipient_email, email_message)

        # Quit the SMTP server
        smtp_server.quit()

        print("Email sent successfully.")
    except Exception as e:
        print(f"Error: {str(e)}")
# Function to send an SMS using Twilio
def send_sms():
    twilio_account_sid = "ACee25965e4895100a7f7a50c0b46208a8"
    twilio_auth_token = '84801f57752db54d14e54ce32d482e92'
    twilio_phone_number ="+13342342930",

    client = Client(twilio_account_sid, twilio_auth_token)
    to_phone_number = input("enter the number ")
    message = input("Enter the SMS message: ")

    try:
        message = client.messages.create(
            body=message,
            from_=twilio_phone_number,
            to=to_phone_number
        )

        print(f"SMS sent to {to_phone_number}: {message.sid}")
    except Exception as e:
        print(f"Failed to send SMS: {str(e)}")

# Main program loop
while True:
    print("\nSelect an option:")
    print("1. Send WhatsApp Message")
    print("2. Send Email")
    print("3. Send SMS")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        send_whatsapp_message()
    elif choice == '2':
        send_email()
    elif choice == '3':
        send_sms()
    elif choice == '4':
        break
    else:
 
        print("Invalid choice. Please select a valid option.")


# In[ ]:




