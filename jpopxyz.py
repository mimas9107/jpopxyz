site_url="https://jpop.xyz/"
# import numpy as np
# import matplotlib.pyplot as plt
import requests
import random
from bs4 import BeautifulSoup as bs
import time
import json
import datetime
import pandas as pd

header1={
    "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0"
}
header2={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
}
header3={
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36"
}
header4={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50"
}

headers_list=[header1,header2,header3,header4]

site_url="https://jpop.xyz/"
page_current:int = 1
page_next:int = page_current + 1
page_max:int = 22
article_current_page_num = page_current
articles_db=[]

while article_current_page_num <page_max:
    headers=random.choice(headers_list)
    session = requests.session()
    resp = session.get(site_url,headers=headers)
    soup = bs(resp.text,'lxml')
    print("****************",site_url," - ",article_current_page_num,"****************")
    #parsing:
    for i in range(len(soup.select("div article"))):
        article_figure_url:str = soup.select("div article")[i].select("figure img")[0]['src']
        article_title:str = soup.select("div article")[i].select("h2 a")[0]['title']
        article_detail_url:str = soup.select("div article")[i].select("h2 a")[0]['href']
#         print("title={},url={},figure={}".format(article_title, article_detail_url,article_figure_url))
        articles_db.append({"title":article_title, "url":article_detail_url, "img":article_figure_url})
#     article_current_page_num:int = int(soup.select("div.nav-links")[0].select("span")[0].text)
    article_next_page_url:str = soup.select("div.nav-links")[0].select("a")[-1]['href']
    
    site_url:str = article_next_page_url
    article_current_page_num +=1
    
    #         delay_choices = [8, 5, 10, 6, 13, 11]
    delay_choices = [5, 3, 4, 6, 2]
    delay = random.choice(delay_choices)
#     print('delay time=',delay,'next=',site_url)
    time.sleep(delay)
    session.close()
    
endl:str = "\n"
Y=datetime.datetime.now().year
M=datetime.datetime.now().month
D=datetime.datetime.now().day
H=datetime.datetime.now().hour
m=datetime.datetime.now().minute
s=datetime.datetime.now().second
# df1.to_csv("output-{}{}{}-{}{}{}.csv".format(Y,M,D,H,m,s))
# df1.to_html("output-{}{}{}-{}{}{}.html".format(Y,M,D,H,m,s))
filename ="output-{}{}{}-{}{}{}.html".format(Y,M,D,H,m,s)
f = open(filename,"w")
f.write("<table border=\"1\" class=\"dataframe\">"+endl)
f.write("<thead>"+endl)
f.write("<tr style=\"text-align: right;\">"+endl)
f.write("<th>img</th>"+endl)
f.write("<th>articles</th>"+endl)
f.write("</tr>"+endl)
f.write("</thead>"+endl)
f.write("<tbody>"+endl)
for i in articles_db:
    f.write("<tr>"+endl)
    f.write("<td><img src=\"{}\" width=\"125\" height=\"125\"></td>".format(i['img']) + endl)
    f.write("<td><a href=\"{}\"> {} </a></td>".format(i['url'],i['title']) + endl)
    f.write("</tr>"+endl)

f.write("</tbody>"+endl)
f.write("</table>"+endl)

            
f.close()
print("Write data into {} finished!".format(filename))
	
