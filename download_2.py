import sys
import io
import urllib.request as req

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#이미지 및 주소
imgUrl ="http://post.phinf.naver.net/20160621_169/1466482468068lmSHj_JPEG/If7GeIbOPZuYwI-GI3xU7ENRrlfI.jpg"
htmlURL ="http://google.com"

# save path 설정
savePath1 ="c:/test1.jpg"
savePath2 ="c:/index.html"

#urlopen 이용하기
f = req.urlopen(imgUrl).read()
f2 = req.urlopen(htmlURL).read()

savefile1 = open(savePath1,'wb') # w: write, r:read, a: add
savefile1.write(f)
savefile1.close()

#with 이용하기
with open(savePath2,'wb') as savefile2:
    savefile2.write(f2)

print("다운로드 완료!")
