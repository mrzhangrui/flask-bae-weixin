#coding=utf-8
import requests

import time,random
from bs4 import BeautifulSoup

def xiaohua():
	url='http://api.avatardata.cn/Joke/QueryJokeByTime'
	page=random.sample(range(300),1)
	data={
		'key':'03ee63eff7d443e299416e07a05c6231',
		'time':str(int(time.time())),
		'sort':'desc',
		'page':page
	}
	re=requests.get(url,params=data).json()['result']
	num=random.sample(range(len(re)),1)
	for i in num:
		content=re[i]['content'].encode('utf-8')
	return content


def fanyi(word):
	url='http://fanyi.youdao.com/openapi.do?keyfrom=zrzj11&key=693191544&type=data&doctype=json&version=1.1&q=%s'%word
	re=requests.get(url).json()
	word=re['query']
	tran=re['translation']
	tran=','.join(tran)
	explains=','.join(re['basic']['explains'])
	content=u'%s\n%s\n网络释义:\n%s'%(word,tran,explains)
	return content

def tianqi(city):
	url='http://api.avatardata.cn/Weather/Query'
	city=city.encode('utf-8')
	data={
		'key':'0cbf803c9d6640ed99b59b70d235baa9',
		'cityname':city
	}
	re=requests.get(url,params=data).json()
	re=re['result']#['realtime']
	#cityname=re['city_name']
	#date=re['date']
	#weather=re['weather']['info']
	#tem=re['weather']['temperature']
	#content=u'城市:%s\\n日期:%s\\n天气:%s\\n温度:%s'%(cityname,date,weather,tem)
	content=city
	return content



