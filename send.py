import smtplib
from email.mime.text import MIMEText

smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
smtp_ssl_port = 465
username = 'haloba.halob'
password = 'azertyuiop123456789'
sender = 'haloba.halob@gmail.com'
targets = ['abdellah.sabry@gmail.com']

msg = MIMEText('ALERT IN POWER STATION!!!')
msg['Subject'] = 'TRAP!'
msg['From'] = sender
msg['To'] = ', '.join(targets)
try:
    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
    server.login(username, password)
    server.sendmail(sender, targets, msg.as_string())
    server.quit()
except Exception, e:
    print e
