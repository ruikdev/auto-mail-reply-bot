import imaplib
import email
import smtplib
import time
from email.mime.text import MIMEText

# Connection parameters for your Infomaniak email account
EMAIL = ""
PASSWORD = ""

# Function to send a reply email
def send_reply(sender_email):
    # Creating the reply message
    reply_message = """AUTO MESSAGE:
Hello,
Thank you for contacting me. I will respond to you as soon as possible.

Useful links:
portfolio:  
discord contact:

PLEASE do not reply to this automatic message.
"""

    try:
        # Configuration of the Infomaniak SMTP server parameters
        smtp_server = 'mail.infomaniak.com'
        smtp_port = 587

        # Connecting to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(EMAIL, PASSWORD)

        # Creating the email
        msg = MIMEText(reply_message)
        msg['Subject'] = 'Automatic Reply'
        msg['From'] = EMAIL
        msg['To'] = sender_email

        # Sending the email
        server.sendmail(EMAIL, sender_email, msg.as_string())

        # Displaying the emails to which an automatic reply was sent
        print(f"Automatic reply sent to: {sender_email}")

        # Closing the connection to the SMTP server
        server.quit()

    except Exception as e:
        # Displaying errors
        print(f"Error sending automatic reply to {sender_email}: {e}")

# Main function to check emails and send replies
def main():
    while True:
        try:
            # Connecting to your Infomaniak inbox
            mail = imaplib.IMAP4_SSL('mail.infomaniak.com')
            mail.login(EMAIL, PASSWORD)
            mail.select('inbox')

            # Searching for unread emails
            result, data = mail.search(None, 'UNSEEN')

            # Iterating over unread emails
            for num in data[0].split():
                result, data = mail.fetch(num, '(RFC822)')
                raw_email = data[0][1]
                msg = email.message_from_bytes(raw_email)

                # Getting the email sender
                sender_email = msg['From']

                # Sending an automatic reply
                send_reply(sender_email)

                # Marking the email as read
                mail.store(num, '+FLAGS', '\\Seen')

            # Closing the IMAP connection
            mail.close()
            mail.logout()

            # Pause for a minute before the next check
            time.sleep(60)

        except Exception as e:
            # Displaying errors
            print(f"An error occurred while checking emails: {e}")

if __name__ == "__main__":
    main()
