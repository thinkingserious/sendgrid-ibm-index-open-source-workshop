import sendgrid
from sendgrid.helpers.mail import *

def build_response(status_code):
    if status_code == 202:
        return {"status": "success"}
    else:
        return {"status": "error"}

def send_email(apikey):
    sg = sendgrid.SendGridAPIClient(apikey=apikey)
    from_email = Email("dx@sendgrid.com")
    to_email = Email("elmer@sendgrid.com")
    subject = "Sending with SendGrid is Fun"
    content = Content("text/plain", "and easy to do anywhere, even with Python")
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    return build_response(response.status_code)
