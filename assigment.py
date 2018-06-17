import sys
import io
import urllib.request as req

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


imgurl = 'https://ssl.pstatic.net/tveta/libs/1194/1194772/d613714f6211db96b582_20180531163813100.jpg'

savepath = 'c:/test2.jpg'

f = req.urlopen(imgurl).read()

with open(savepath,'wb') as savefile:
    savefile.write(f)

print('다운로드 완료')
