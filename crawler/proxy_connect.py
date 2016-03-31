import urllib.request

# set up authentication info
authinfo = urllib.request.HTTPBasicAuthHandler()

proxy_support = urllib.request.ProxyHandler({'http': 'http://chaulh:123456@proxy.tsdv.com.vn:3128'})

# build a new opener that adds authentication and caching FTP handlers
opener = urllib.request.build_opener(proxy_support, authinfo,
                                     urllib.request.CacheFTPHandler)

# install it
urllib.request.install_opener(opener)
url = 'http://www-rohan.sdsu.edu/~gawron/index.html'
f = urllib.request.urlopen(url)
print(f.read()[:150])
