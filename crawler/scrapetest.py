from urllib import *

proxy = urllib.request.ProxyHandler({'http': 'http://chaulh:123456@proxy.tsdv.com.vn:3128'})
auth = urllib.request.HTTPBasicAuthHandler()
opener = urllib.build_opener(proxy, auth, urllib.request.HTTPHandler)
urllib.install_opener(opener)

conn = urllib.urlopen('http://google.com')
return_str = conn.read()
