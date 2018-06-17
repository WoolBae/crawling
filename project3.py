from bs4 import BeautifulSoup
import sys
import io
import urllib.request as req
import urllib.parse  as rew
import os
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


url ='https://www.inflearn.com/'
res = req.urlopen(url).read()
soup = BeautifulSoup(res, 'html.parser')


#유니코드로 바꾸기
# quote = rew.quote_plus("추천-강좌")
# print(quote)
savepath = 'C:/imagedown/'
img_list = soup.select('ul.grid')[1]
for i, e in enumerate(img_list,1):
    with open(savepath+'text_' +str(i) +'.txt',"wt")as f:
        f.write(e.select_one("h4.block_title > a").string)
    fullfilename = os.path.join(savepath, str(i) +'.png')
    req.urlretrieve(e.select_one("div.block_media > a > img")['src'],fullfilename)

print('다운로드 완료')
