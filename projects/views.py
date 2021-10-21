import projects
from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
import pandas as pd
import requests
import bs4
from IPython.display import HTML
import time
from random import randint
from random import choice
from random import sample
import sqlite3 as sq

#sets up soup to get data for spanish tools
letters = ["a","b","c","d"]
result = requests.get('https://www.spanishdict.com/wordoftheday/1')
soup = bs4.BeautifulSoup(result.text,'lxml')

#gets Coin Market Cap homepage and converts to beautiful soup object
result2 = requests.get("https://coinmarketcap.com/")
soup2 = bs4.BeautifulSoup(result2.text,'lxml')


# Create your views here.
def home(request):
    allprojects = Project.objects.all()
    return render(request,'projects/homepage.html', {'allprojects':allprojects})

def project(request):
    allprojects = Project.objects.all()
    return render(request,'projects/projects.html', {'allprojects':allprojects})

def about(request):
    return render(request,'projects/about.html')

def contact(request):
    return render(request,'projects/contact.html')

def udemy(request):
    return render(request,'projects/udemy.html')

def pong(request):
    return render(request,'projects/pong.html')

def spanish(request):
    return render(request,'projects/spanish.html')

def spanish2(request):
    theselection = request.GET.get('selection')
    thedisplay = ''
    if theselection == 1:
        today = soup.select('h3')[0]
        totext = today.text
        today1 = soup.select('div._3iXmZ8Jd')[0]
        totext1 = today1.text
        spex = soup.select("div._2I4LpW3B")[0]
        spextext = spex.text
        enex = soup.select('div._2w_JRz6o')[0]
        enextext = enex.text

        thedisplay += "<p>testing<p>"
    else:
        pass
    return render(request,'projects/spanish2.html', {'thedisplay':thedisplay})



result2 = requests.get("https://coinmarketcap.com/")
soup2 = bs4.BeautifulSoup(result2.text,'lxml')

def cryptos(request):

    names = []
    for name in soup2.select('.iJjGCS')[8:]:
        names.append(name.text)

    #grabs tickers
    symbols = []
    for syms in soup2.select('.gGIpIK')[:]:
        symbols.append(syms.text)


    prices = []
    for price in soup2.select('div.sc-131di3y-0.cLgOOr')[0:]:
        prices.append(price.text)

    caps = []
    for cap in soup2.select('span.sc-1ow4cwt-1.ieFnWP'):
        caps.append(cap.text)

    data = {'Name':names,
            'Ticker': symbols,
            'Price': prices,
            'Market Cap': caps}

    df = pd.DataFrame(data, columns=['Name','Ticker','Price','Market Cap'])
    df = df.set_index([pd.Index(['1', '2', '3', '4', '5', '6', '7', '8','9','10'])])
    allcryptos = df.to_html()
    return HttpResponse(allcryptos)
