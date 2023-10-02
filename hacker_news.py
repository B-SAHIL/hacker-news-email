import requests
# Web scraping
from bs4 import BeautifulSoup
# Send email
import smtplib
# Email body
from email.mime.multipart import MIMEMultipart
from email .mime.text import MIMEText

# system date and time
import datetime
now = datetime.datetime.now()

msg = MIMEMultipart()



def extract_news(url):
    print('Extreacting Hacker News Stories......')
    cnt = ''
    cnt = ('<b>HN Top Stories:<b>\n '+' <br>'+ '_' *50 +' <br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    for i, tag in enumerate(soup.find_all('td', attrs={
        'class': 'title', 'valign': ''
    })):
        cnt += ((str(i+1) + ':: '+ tag.text+ '\n' + '<br>') if tag.text != 'More' else '')
    return cnt



def send_email(FROM, TO, SERVER, PORT, PASS):
    content = ''
    cnt = extract_news(url='https://news.ycombinator.com/')
    content += cnt  
    content += ('<br>____________________<br>')
    content += ('<br><br> Thank you.')
    content += ('<a href="mailto:yagitsahil@gmial.com">Send Email</a>')
    msg['subject'] = 'Top News Stories HN [Automated email]' + '' + str(now.day) + '-' + str(now.month)+ '-' +  str(now.year)
    msg['From'] = FROM
    msg['To'] = TO
    msg.attach(MIMEText(content, 'html'))
    print('Starting server.............')
    server = smtplib.SMTP(SERVER, PORT)
    server.set_debuglevel(1)
    server.ehlo()
    server.starttls()
    server.login(FROM, PASS)
    server.sendmail(FROM, TO, msg.as_string())
    print('Email sent..............')
    server.quit()
