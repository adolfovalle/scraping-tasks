import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from django.http import HttpResponse
from task2.models import VideoArticle

def index(request):
    url = 'https://elpais.com'
    r = requests.get(url)
    coverpage = r.content
    soup = BeautifulSoup(coverpage, 'html5lib')
    video_icons = soup.find_all('svg', class_="icon_multimedia_video")    
    print(video_icons)
    for icon in video_icons:
        video_article_url = url+icon.parent.parent.get('href')

        r2 = requests.get(video_article_url)
        video_article = r2.content
        soup2 = BeautifulSoup(video_article, 'html5lib')

        titulo = soup2.find('h1', class_="a_t").get_text()
        fecha = soup2.find('a', class_="a_ti").get_text()
        texto = soup2.find('div', class_="article_body").get_text()

        v = VideoArticle(url = video_article_url, titulo=titulo, texto=texto, fecha=fecha)
        v.save()


        data = soup2.find_all('script',type="application/javascript")
        print(data[3].find('sourcePath'))

    return HttpResponse("Hecho")