
from bs4 import BeautifulSoup
import urllib.request
import re

def find_by_tag_div( soup ):
    topic_link = []
    for element in soup.find_all('div',{'class':'col-sm-4 col-md-4'}):
        for link in element.find_all('a'):
            # print(link.get_text())
            # print(link['href'])
            topic_link.append(link['href'])
    return topic_link


def find_by_link(soup):
    for link in soup.find_all(href=re.compile("topic")):
        print(link['href'])
web_domain = 'http://www.brainyquote.com'
url = web_domain + "/quotes/topics.html"
# html_path = "http://www.google.com"
req = urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
html_doc = urllib.request.urlopen(req)
# print(html_doc.read())
soup = BeautifulSoup(html_doc, 'html.parser')
topic_link = find_by_tag_div(soup)
print(topic_link[0])

url = web_domain + topic_link[0]
print(url)
req = urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
html_doc = urllib.request.urlopen(req)
soup = BeautifulSoup(html_doc,'html.parser')
quotes_list = soup.find_all('div',{'id':'quotesList'})[0]
# # print(quotes_list.find_all('a'))
# for quote in quotes_list.find_all('a',{'title':{'view quote','view author'}}):
#     print(quote.get_text())
navigation_tab = soup.find_all('ul',{'class':'pagination bqNPgn pagination-sm '})

navigation_link = navigation_tab[0].find_all(href=re.compile('topic'))

max = -1 
for link in navigation_link:
    print(link.get_text())
    if link.get_text()!='Next':
        if int(link.get_text()) > max:
            max = int(link.get_text())


print(max)