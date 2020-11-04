import sys
import urllib.request as req
import urllib.parse as parse  # url 인코딩

# 명령줄 인수가 제대로 입력 되었는지 확인
if len(sys.argv) <=1: # 명령줄 인수가 1이하이면 오류 메시지 출력
    print("사용법 : python 인수1 인수2")
    sys.exit()
    
regionCode = sys.argv[1]
    
rssUrl = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"

values = {
    'stnId':regionCode
}

params = parse.urlencode(values)

url = rssUrl + "?" + params

print("url = ",url)

# rss 데이터를 다운로드
data = req.urlopen(url).read()
text = data.decode("utf-8")

print(text)
