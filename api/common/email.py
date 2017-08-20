import smtplib

def send_email(user, pwd, recipient, subject, body):
    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (user, recipient, subject, body)

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(user, recipient, message)
        server.close()
    except Exception as e:
        print(str(e))