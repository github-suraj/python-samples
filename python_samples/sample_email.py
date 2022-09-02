'''
    Module File for sending Emails
'''

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

class SendEmail:
    """
        Class for sending emails:
            Different email service providers dtails:
                1. Gmail: smtp.gmail.com:587
                2. Outlook: smtp-mail.outlook.com:587
                3. Office 365: outlook.office365.com
    """
    def __init__(
            self,
            body,
            subject,
            toemails,
            fromemail,
            fromemail_pass,
            filenames=None
        ):
            self.body = body
            self.subject = subject
            self.toemails = toemails
            self.fromemail = fromemail
            self.fromemail_pass = fromemail_pass
            self.filenames = filenames

    @staticmethod
    def get_file_instance(filename):
        '''
            Static Method to create file instance for attachment
        '''
        p = MIMEBase('application', 'octet-stream')
        p.set_payload(open(filename, "rb").read())
        encoders.encode_base64(p)
        fname = os.path.split(filename)[-1]
        p.add_header('Content-Disposition', f"attachment; filename={fname}")
        return p

    def get_message(self):
        '''
            Method to create email message string 
        '''
        msg = MIMEMultipart()
        msg['From'] = self.fromemail
        msg['To'] = self.toemails
        msg['Subject'] = self.subject
        msg.attach(MIMEText(self.body, 'html'))
        for filename in self.filenames:
            msg.attach(self.get_file_instance(filename))
        return msg.as_string()

    def __call__(self):
        try:
            client = smtplib.SMTP('smtp.gmail.com', 587)
            client.starttls()
            client.login(self.fromemail, self.fromemail_pass)
            print(f'Sending Mail\n\tFrom: {self.fromemail}\n\tTo: {self.toemails}')
            client.sendmail(self.fromemail, self.toemails, self.get_message())
            print('Sent Mail Successfully!')
            client.quit()
        except Exception as error:
            print(f'Sending Mail Failed with [{error}]')


if __name__ == '__main__':
    from_email = os.environ['FROM_EMAIL']
    from_email_pass = os.environ['FROM_EMAIL_PASS']
    to_emails = os.environ['TO_EMAILS']
    files = [
        os.path.join('sample_docs', 'email', filename)
        for filename in ['email_file1.txt', 'email_file2.xlsx']
    ]
    SUBJECT = "Testing email with Python"
    BODY = """<html>
                   <head>Hi All,</head>
                   <body>
                      <p>This is a sample Email, PFA file.</p><br>
                      <br>Thanks,<br>John Wick.<br>
                   </body>
                </html>"""
    SendEmail(BODY, SUBJECT, to_emails, from_email, from_email_pass, files)()
