import app
import os

def main(args):
    apikey = args.get("SENDGRID_API_KEY")
    return app.send_email(apikey)
