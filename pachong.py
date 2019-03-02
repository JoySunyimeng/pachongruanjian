import time
import requests
from bs4 import BeautifulSoup

#下面是字典
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
#下面是循环一到十二
for i in range (1, 13):
    time.sleep(5)
    #把1转换为01
    url = 'http://www.tianqihoubao.com/aqi/beijing-2018' + str("%02d" % 1) + '.html'
    #返回文本
    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text,'html.parser')
    # tr代表列 td代表行
    tr = soup.find_all('tr')
    #去除标签栏
    for j in tr[i:]:
        td = j.find_all('td')
        #把以下内容存入变量
        Date = td[0].get_text().strip()
        Quality_grade = td [1].get_text().strip()
        AQI = td[2].get_text().strip()
        AQI_rank = td[3].get_text().strip()
        PM = td[4].get_text()
        #打开文件吧每行内容 拼成字符串存入文件
        with open ('air_Beijing_2018.csv ', 'a+', encoding='utf-8-sig')as f:
            f.write(Date +','+ Quality_grade + ','+ AQI+ ',' + AQI_rank + ','
            + PM +'\n')




