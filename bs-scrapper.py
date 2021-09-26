import requests #http requests

from bs4 import BeautifulSoup # web scrapping

import smtplib
#email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#system date and time manipulation
import datetime

now = datetime.datetime.now()

# email content placholder
content = ''

#extractin Hacker News Stories

def extract_news(url):
    print('Extractin Hacker News Stories...')
    cnt = ''
    cnt +=('<b>HN Top Stories:</b>\n'+'<br>'+'-'*50+'<br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content,'html.parser')
    for i,tag in enumerate(soup.find_all('td',attrs={'class':'title','valign':''})):
        cnt += ((str(i+1)+' :: '+tag.text + "\n" + '<br>') if tag.text !='More' else '')
    return(cnt)

try:
    cnt = extract_news('https://news.ycombinator.com/')
    content += cnt
    content += ('<br>-------<br>')

except FileNotFoundError:

    print( "file not found")

#lets send the email

print('Composing Email...')

SERVER = 'smtp.gmail.com'
PORT = 587
FROM = 'kirktolliver28@gmail.com'
TO = 'kirktolliver23@gmail.com'
PASS = ''

msg = MIMEMultipart()
