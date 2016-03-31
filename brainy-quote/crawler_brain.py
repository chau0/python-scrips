from bs4 import BeautifulSoup
import urllib.request
import re

def open_web(url):
    authinfo = urllib.request.HTTPBasicAuthHandler()
    proxy_support = urllib.request.ProxyHandler({'http': 'http://chaulh:123456@proxy.tsdv.com.vn:3128'})
    opener = urllib.request.build_opener(proxy_support, authinfo,urllib.request.CacheFTPHandler)
    urllib.request.install_opener(opener)
    req = urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
    html_doc = urllib.request.urlopen(req)
    return html_doc

def get_list_topic(soup):
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

def get_navigation_link(soup):
    navigation_tab = soup.find_all('ul',{'class':'pagination bqNPgn pagination-sm '})
    navigation_link = navigation_tab[0].find_all(href=re.compile('topic'))
    return navigation_link

def get_number_page(navigation_link):
    max = -1
    for link in navigation_link:
        # print(link.get_text())
        if link.get_text()!='Next':
            if int(link.get_text()) > max:
                max = int(link.get_text())
    return max


web_domain = 'http://www.brainyquote.com'
url = web_domain + "/quotes/topics.html"
html_doc = open_web(url)
# print(html_doc.read())
soup = BeautifulSoup(html_doc, 'html.parser')
topic_link = get_list_topic(soup)
file_writer = open('quote.txt', 'w')
for topic in topic_link:
    url = web_domain + topic
    print(url)
    html_doc = open_web(url)
    soup = BeautifulSoup(html_doc,'html.parser')
    quotes_list = soup.find_all('div',{'id':'quotesList'})[0]
    navigation_link = get_navigation_link(soup)
    number_page = get_number_page(navigation_link)
    for page in range(0,number_page):
        url = web_domain + topic + str(page)
        print(url)
        # print(quotes_list.find_all('a'))
        for quote in quotes_list.find_all('a',{'title':{'view quote','view author'}}):
            print(quote.get_text())
            file_writer.write(quote.get_text()+"\n")

#
 # print(quotes_list.find_all('a'))
# for quote in quotes_list.find_all('a',{'title':{'view quote','view author'}}):
#     print(quote.get_text())
