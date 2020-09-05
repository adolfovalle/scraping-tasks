import requests
import time
from django.db import IntegrityError
from bs4 import BeautifulSoup
from django.shortcuts import render
from django.http import HttpResponse
from task2.models import VideoArticle
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager




def index(request):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver.exe', chrome_options=options)
    url = 'https://elpais.com'

    r = driver.get(url)
    time.sleep(20)
    html = driver.page_source
    driver.quit()
    
    # coverpage = r.content
    soup = BeautifulSoup(html, 'html5lib')
    icons = soup.find_all("svg")    
    #print(icons)
    #find icons
    for icon in icons:
        video_article_url =""
        #filter if video icon
        if('icon_multimedia_video' in icon['class']):
            print(icon['class'])
            #get video url
            for parent in icon.parents:
                tagType = parent.name
                print(tagType)
                if(tagType=='a'):
                    aref = parent['href']
                    if(aref.startswith("http")):
                        video_article_url = aref
                        print(aref)
                    else:
                        video_article_url = url+aref
                        print(video_article_url)
                    break

            r2 = requests.get(video_article_url)
            video_article = r2.content
            soup2 = BeautifulSoup(video_article, 'html5lib')

            titulo = soup2.find('h1', class_="a_t").get_text()
            fecha = soup2.find('a', class_="a_ti").get_text()
            texto = soup2.find('div', class_="article_body").get_text()

            
            try:
                v = VideoArticle(url = video_article_url, titulo=titulo, texto=texto, fecha=fecha)
                v.save()
                data = soup2.find_all('script',type="application/javascript")
                stringVideo = data[3].get_text()
                sourcepathIndex = stringVideo.find("sourcePath")+len("sourcePath")+3
                extensionIndex = stringVideo.find(".mp4")+len(".mp4")
                url_video = stringVideo[sourcepathIndex: extensionIndex]
                print(url_video)
                rVideo = requests.get(url_video, allow_redirects=True)
                open(titulo+".mp4", 'wb').write(rVideo.content)
                print("video "+titulo+" descargado") 
            except IntegrityError as e: 
                print("Ha fallado el ingreso a la base de datos")



    return HttpResponse("Hecho")