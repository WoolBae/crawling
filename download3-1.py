import sys
import io
import urllib.request as req
from urllib.parse import urlparse

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "http://www.encar.com"

mem = req.urlopen(url)
print(mem)

print(type({}))
print(type(()))
print(type([]))


print('geturl',mem.geturl())
print('status',mem.status) #200(정상), 404(없음),403(거절), 500(문제있음)
print('headers',mem.getheaders())
print("")
print('info', mem.info())
print("code",mem.getcode())
print("read",mem.read(50).decode('utf-8')) # 정석적으로 decode 붙인다.

print(urlparse("http://www.encar.com?test=test"))
