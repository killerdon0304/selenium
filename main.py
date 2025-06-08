import json
import time
from req import scrap

baseurl = "https://netfree2.cc/mobile/"
otts = ["nf","pv"]
pages= ["home","series","movies"]


for ott in otts:
    print(ott)
    allData ={}
    allData["time"]=time.ctime(time.time())
    for page in pages:
        url = baseurl + page
        print(url)
        # exit()
        soup= scrap(url,ott)

        dist = {}
        # sliders= soup.find_all("div", class_="temp-hide")
        sliders = soup.select("div.temp-hide")
        sliderList=[]
        for slider in sliders:
            movie=slider["onclick"].split("'")[1]
            sliderList.append(movie)
        dist["slider"]=sliderList

        ## Top10 movie section
        t10List =soup.find_all("div", class_="top10")
        Topmovie={}
        for t10 in t10List:
            category=t10.span.string
            allT10 = t10.find_all("div", class_="top10-post")
            a=[]
            for aT10 in allT10:
                a.append(aT10["data-post"])
            Topmovie[category] = a
        dist["top10"] = Topmovie
        # print(Topmovie)


        # exit()
        a=soup.find_all("div",class_="tray-container")
        mmovie={}
        for x in a:
            category = x.find("a", class_="tray-link").string
            articles = x.find_all("article")
            movies = []
            for article in articles:
                movie = article.find('a')['data-post']
                movies.append(movie)
            
            mmovie[category] = movies
        dist["movies"]=mmovie

        # print(a[0].find_all("article")[0].find('a')['data-post'])
        # print(dist)
        allData[page]= dist
        time.sleep(10)
    with open(f"{ott}.json", "w") as f:
        json.dump(allData, f, indent=4)
    time.sleep(10)
