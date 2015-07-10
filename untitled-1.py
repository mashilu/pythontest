import urllib.request

sock = urllib.request.urlopen("http://www.baidu.com")
htmlsource = sock.read()
sock.close
print(htmlsource)