import pytube
import os
import subprocess
# 다운 받을 동영상 url 지정
yt = pytube.YouTube('https://www.youtube.com/watch?v=Kbj2Zss-5GY')

videos = yt.streams.all()

for i in range(len(videos)):
    print(i,',',videos[i])

down_dir = "C:\YouTube"


cnum =int(input("다운 받을 화질은(0~21 입력)"))

videos[cnum].download(down_dir)

newfilename =input('변환할 mp3 파일명은?')
originalfilename =videos[cnum].default_filename



subprocess.call(['ffmpeg', '-i',
os.path.join(down_dir,originalfilename),
os.path.join(down_dir,newfilename)])


print('동영상 다운로드 및 mp3 변환완료')
