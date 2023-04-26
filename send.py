import smtplib
import findNewPost
from email.mime.text import MIMEText

def getSmtpInfo ():
    try:
        with open("password.txt","r", encoding="utf-8") as file:
            a = file.readlines()

            return a[0].strip(),a[1].strip()
       
    except FileNotFoundError:
        print(">>>>  There is no password file.")
        raise FileNotFoundError


def create_content(oldContent : str,newContent : str):
    result = []
    wordStarLine = "*"*22
    starLine = "*" * 55
    newPosts = findNewPost.find_newPost(oldContent,newContent)

    result.append("퍼즐앤드래곤 공식 사이트의 업데이트가 감지되었습니다. \n\n")
    result.append(wordStarLine +" 새로 업데이트된 공지사항"+wordStarLine)
    for np in newPosts:
        result.append("%d %s %s" %(np[0],np[1],np[2].strftime("%Y-%m-%d")))
    result.append("\n\n")
    result.append(wordStarLine +" New Data"+wordStarLine)
    result.append(newContent)
    result.append(starLine)
    result.append("\n\n")
    result.append(wordStarLine+" Old Data "+wordStarLine)
    result.append(oldContent)
    result.append(starLine)
    result.append("\n")
    result.append("퍼즐앤드래곤 공식 홈페이지 사이트 링크: " + "https://pad.neocyon.com/W/notice/list.aspx")
    return "\n".join(result)

def send_email(oldContent : str,newContent : str):
    

    email, password = getSmtpInfo()
    
    title = "[업데이트 감지] 퍼드 사이트 신규 업데이트 확인"

    smtp2 = smtplib.SMTP('smtp.gmail.com', 587)

    # 서버 연결을 설정하는 단계
    smtp2.ehlo()
    
    # 연결을 암호화
    smtp2.starttls()
    smtp2.login(email, smtp2.login(email, password))


    content = create_content(oldContent=oldContent,newContent=newContent)
    msg = MIMEText(content)

    msg['From'] = email
    msg['To'] = email
    msg['Subject'] = title

    smtp2.sendmail(email, email, msg.as_string())
    smtp2.close()

if __name__ == "__main__":
    

    send_email("".join(findNewPost.getOldContent()),"".join(findNewPost.getTempNew()))