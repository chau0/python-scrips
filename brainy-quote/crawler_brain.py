from bs4 import BeautifulSoup
import urllib.request
import re
from database import MongoConnector

def open_web(url,is_proxy):
    if is_proxy:
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

def get_quote_list(url,is_proxy):
    html_doc = open_web(url,is_proxy)
    soup = BeautifulSoup(html_doc,'html.parser')
    quotes_list = soup.find_all('div',{'id':'quotesList'})[0]
    return quotes_list



is_proxy = False
web_domain = 'http://www.brainyquote.com'
url = web_domain + "/quotes/topics.html"
html_doc = open_web(url,is_proxy)
db_connector = MongoConnector('localhost',27017,'brainy','quotes')

# print(html_doc.read())
soup = BeautifulSoup(html_doc, 'html.parser')
topic_link = get_list_topic(soup)
file_writer = open('quote.txt', 'w')
for topic in topic_link:
    url = web_domain + topic
    print(url)
    html_doc = open_web(url,is_proxy)
    soup = BeautifulSoup(html_doc,'html.parser')
    navigation_link = get_navigation_link(soup)
    number_page = get_number_page(navigation_link)

    for page in range(1 , number_page + 1):
        if page == 0:
            url = web_domain + topic
        else:
            url = web_domain + topic + str(page)

        print(url)
        quotes_list = get_quote_list(url,is_proxy)
        # print(quotes_list.find_all('a'))
        quote_author = ''
        quote_content= ''
        for quote in quotes_list.find_all('a',{'title':{'view quote','view author'}}):
            # print(quote['title'])
            if quote_content:
                quote_author = quote.get_text() 
            if not quote_content:
                quote_content = quote.get_text() 
            # file_writer.write(quote.get_text()+"\n")
            if quote_author and quote_content:
                quote_topic = topic.split('_')[1].split('.')[0]
                db_connector.insert_quote(quote_author,quote_content,quote_topic)
                quote_author  = ''
                quote_content = ''


#
 # print(quotes_list.find_all('a'))
# for quote in quotes_list.find_all('a',{'title':{'view quote','view author'}}):
#     print(quote.get_text())
