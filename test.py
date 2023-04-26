import smtplib
from email.mime.text import MIMEText

recv_email = 'livedfognis@gmail.com'
smtp_gmail = smtplib.SMTP('smtp.gmail.com', 587)

# 서버 연결을 설정하는 단계
smtp_gmail.ehlo()
 
# 연결을 암호화
smtp_gmail.starttls()
 
#로그인
smtp_gmail.login('livedfognis@gmail.com','xpimksjwqpfwuifs')

content = "Text!"
msg = MIMEText(content)

msg['From'] = recv_email
msg['To'] = recv_email
msg['Subject'] = "title"

smtp_gmail.sendmail(recv_email, recv_email, msg.as_string())
smtp_gmail.close()