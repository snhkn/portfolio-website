import smtplib, ssl

host = "smtp.gmail.com"
port = 465

user_name = "snhknprojects@gmail.com"
password = "qkbxdjxutnxinkea"

receiver = "snhknprojects@gmail.com"
context = ssl.create_default_context()

message = """\
Subject: Hi!
How are you?
Bye!
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(user_name, password)
    server.sendmail(user_name, receiver, message)
