import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

EMAIL_SENDER   = "ashishkailskirde@gmail.com"
EMAIL_PASSWORD = "oiejyabuzvazvith"

msg = MIMEMultipart("alternative")
msg["Subject"] = "✅ Beyond Class - Email Test"
msg["From"]    = EMAIL_SENDER
msg["To"]      = EMAIL_SENDER  # sends to yourself

msg.attach(MIMEText("<h2>Email is working! 🎉</h2>", "html"))

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(EMAIL_SENDER, EMAIL_PASSWORD)
server.sendmail(EMAIL_SENDER, EMAIL_SENDER, msg.as_string())
server.quit()

print("✅ Email sent successfully!")