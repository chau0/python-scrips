import os,bs4
import urllib.request

url='http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
    print('Downloading page %s...'% url)
    authinfo = urllib.request.HTTPBasicAuthHandler()
    proxy_support = urllib.request.ProxyHandler({'http': 'http://chaulh:123456@proxy.tsdv.com.vn:3128'})
    opener = urllib.request.build_opener(proxy_support, authinfo,
                                         urllib.request.CacheFTPHandler)
    urllib.request.install_opener(opener)
    web = urllib.request.urlopen(url)
    soup= bs4.BeautifulSoup(web.read(),'html5lib')

    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = "http:"+comicElem[0].get('src')
        image_name = comicUrl.split("/")[-1]
        print('Downloading image %s...' % (comicUrl))
        print('image name ... %s'%image_name)
        urllib.request.urlretrieve(comicUrl,os.path.join('xkcd',image_name))
        prevLink = soup.select('a[rel="prev"]')[0]
        url = 'http://xkcd.com' + prevLink.get('href')
print('Done.')
