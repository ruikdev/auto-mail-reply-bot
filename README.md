# auto-mail-reply-bot
A bot that connects to your email address to automatically reply to your emails.



Email Auto-Reply Script

This Python script automates the process of checking an email inbox and sending an automatic reply to unread emails using IMAP and SMTP. It is designed to work with Infomaniak email accounts but can be adapted for other email providers.
How It Works

    Libraries and Modules:
        imaplib: Connects to and interacts with an IMAP email server to check for unread emails.
        email: Parses email messages.
        smtplib: Sends emails via an SMTP server.
        time: Pauses the script between email checks.
        MIMEText: Creates plain text email messages.

    Main Components:
        send_reply(sender_email):
            Creates and sends an automatic reply to the sender's email.
            Connects to the SMTP server, logs in, and sends the reply email.
            Closes the SMTP server connection after sending the email.
        main():
            Connects to the IMAP server and logs in.
            Searches for unread emails in the inbox.
            For each unread email, extracts the sender's email address and sends an automatic reply.
            Marks the email as read.
            Pauses for 60 seconds before repeating the process.

Installation and Configuration

    Install Python:
    Ensure you have Python 3.x installed on your machine. You can download it from python.org.

    Install Required Libraries:
    Use pip to install the required libraries:



pip install secure-smtplib

Set Up Your Email Account:

    Open the auto_reply.py script in a text editor.
    Replace the EMAIL and PASSWORD variables with your Infomaniak email address and password:

    python

    EMAIL = "your_email@example.com"
    PASSWORD = "your_password"

Configure Email Account Settings:
Ensure your email account settings allow access via IMAP and SMTP. For some providers, you may need to enable "Allow less secure apps" or create an app-specific password.

Run the Script:
Save the script and run it using Python:



    python auto_reply.py

    The script will:
        Connect to your email inbox.
        Search for unread emails.
        Send an automatic reply to each unread email.
        Mark emails as read after replying.
        Repeat the process every minute.

Example Auto-Reply Message

The script sends the following automatic reply to unread emails:

vbnet

AUTO MESSAGE:
Hello,
Thank you for contacting me. I will respond to you as soon as possible.

Useful links:
portfolio:  
discord contact:

PLEASE do not reply to this automatic message.

You can customize this message by editing the reply_message variable in the send_reply function.
Error Handling

The script includes error handling to print error messages if something goes wrong during the email checking or replying process. This helps in diagnosing issues such as incorrect login credentials or network problems.
