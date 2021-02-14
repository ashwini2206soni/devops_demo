from synthesize import text_to_mp3
import urllib.request
from bs4 import BeautifulSoup

def html_to_text(url):
    
    with urllib.request.urlopen(url) as web_page:
        html = web_page.read()
        
    soup = BeautifulSoup(html,"html.parser")
    text = ""
    slots = soup.find(attrs={"itemprop" : "headline"})
    text= slots.get_text().lstrip().rstrip()
    slots = soup.find(attrs={"class":"resume-article"})
    slots = slots.find('p')
    text= text +". "+slots.get_text().lstrip().rstrip()
    slots = soup.find(attrs={"class":"content-article blogue"})

    text = text +". ".join(x.get_text() for x in slots.contents if x != "\n")

    return text_to_mp3("en-US-Wavenet-D", text)