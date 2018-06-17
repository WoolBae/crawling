from urllib.parse import urljoin

baseUrl ='http://test.com/html/a.html'

print(">>", urljoin(baseUrl,"b.html"))
print(">>", urljoin(baseUrl,'sub/b.html'))
print(">>", urljoin(baseUrl, "../index.html")) #.. 앞으로 이동 >> http://test.com/index.html
print(">>", urljoin(baseUrl, "../img/img.jpg"))
