#coding=utf-8
from flask import Flask,request,make_response
import hashlib
import xml.etree.ElementTree as ET
import time
from func import *

app=Flask(__name__)
app.debug=True

@app.route('/',methods=['GET','POST'])
def wxapp():
	if request.method=='GET':
		token='zrzj'
		data=request.args
		signature=data.get('signature','')
		timestamp=data.get('timestamp','')
		nonce=data.get('nonce','')
		echostr=data.get('echostr','')
		s=[timestamp,nonce,token]
		s.sort()
		s=''.join(s)
		if (hashlib.sha1(s.encode('utf-8')).hexdigest()==signature):
			return make_response(echostr)
		else:
			rec=request.data
			xml_rec=ET.fromstring(rec)
			ToUserName=xml_rec.find('ToUserName').text
			FromUserName=xml_rec.find('FromUserName').text
			content=xml_rec.find('Content').text
			#构造一个回复
			relay='''
					<xml>
					<ToUserName><![CDATA[%s]]></ToUserName>
					<FromUserName><!CDATA[%s]></FromUserName>
					<CreateTime>%s</CreateTime>
					<MsgType><!CDATA[%s]></MsgType>
					<Content><!CDATA[%s]></Contant>
					<FuncFlag>0<.FuncFlog>
					</xml>
				'''
			if rec.find('MsgType').text =='text':
				if Content.lower()==u'笑话':
					content=xiaohua()

				elif u'天气' in content.lower():
					city=content.strip(u'-天气')
					if city:
						content=tianqi(city)
					else:
						content='请输入查询地址(例：湖北武汉-天气)'

				else:
					content=fanyi(content)

			else:
				Content='暂不支持非文本格式'

			response=make_response(reply%(FromUserName,ToUserName,str(int(time.time)),conntent))
			response.content_type='application/xml'
			return response
if __name__=='__main__':
	app.run()