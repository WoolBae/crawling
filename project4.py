from bs4 import BeautifulSoup
import sys
import io
import os
import urllib.request as req
import urllib.parse  as rep
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')



base ='https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
quote = rep.quote_plus('구글')

url = base + quote
res = req.urlopen(url).read()
savepath = 'C:/imagedown/'


#예외처리
try:
    if not (os.path.isdir(savepath)):
        os.makedirs(os.path.join(savepath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴덜 만들기 실패")
        raise

soup = BeautifulSoup(res, 'html.parser')

img_list = soup.select("div.img_area > a.thumb._thumb > img ")

for i ,img_list in enumerate(img_list,1):
#저장할 파일이름 만들기
    fullfilename = os.path.join(savepath, str(i)+ '.jpg')

    req.urlretrieve(img_list['data-source'],fullfilename)

print('다운로드 완료')
