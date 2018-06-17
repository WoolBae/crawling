from bs4 import BeautifulSoup
import sys
import io
import urllib.request as req
import urllib.parse  as rew
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#
url ='https://www.daum.net/'
res = req.urlopen(url).read()
soup = BeautifulSoup(res, 'html.parser')

top10 = soup.select('div.realtime_part > .list_hotissue.issue_row > li > div >  div[aria-hidden="true"] >  span.txt_issue > a')


for j,i in enumerate(top10,1):
    print(j,i.string)
