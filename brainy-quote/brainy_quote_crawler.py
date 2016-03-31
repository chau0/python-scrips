from bs4 import BeautifulSoup
import urllib.request
import re

authinfo = urllib.request.HTTPBasicAuthHandler()
proxy_support = urllib.request.ProxyHandler({'http': 'http://chaulh:123456@proxy.tsdv.com.vn:3128'})
opener = urllib.request.build_opener(proxy_support, authinfo,
                                     urllib.request.CacheFTPHandler)
urllib.request.install_opener(opener)
web_domain = 'http://www.brainyquote.com'
url = web_domain + "/quotes/topics.html"
req = urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
html_doc = urllib.request.urlopen(req)
print(html_doc.read())
