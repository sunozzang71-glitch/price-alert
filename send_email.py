import os
import smtplib
from email.message import EmailMessage

SENDER_EMAIL = os.environ["SENDER_EMAIL"]
SENDER_APP_PASSWORD = os.environ["SENDER_APP_PASSWORD"]
RECEIVER_EMAIL = os.environ["RECEIVER_EMAIL"]

msg = EmailMessage()
msg["Subject"] = "[테스트] 가격 리포트"
msg["From"] = SENDER_EMAIL
msg["To"] = RECEIVER_EMAIL

msg.set_content("첨부파일 확인해주세요.")

with open("report.csv", "rb") as f:
    msg.add_attachment(f.read(), maintype="text", subtype="csv", filename="report.csv")

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(SENDER_EMAIL, SENDER_APP_PASSWORD)
    smtp.send_message(msg)

print("메일 발송 완료")
