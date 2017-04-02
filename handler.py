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
		echostr=data.get('echostr','huanying')
		s=[timestamp,nonce,token]
		s.sort()
		s=''.join(s)
		if (hashlib.sha1(s.encode('utf-8')).hexdigest()==signature):
			return make_response(echostr)
		else:
			return echostr
	else:
		rec=request.data
		xml_rec=ET.fromstring(rec)
		ToUserName=xml_rec.find('ToUserName').text
		FromUserName=xml_rec.find('FromUserName').text
		Content=xml_rec.find('Content').text.encode('utf-8')
		print(Content)
		#构造一个回复
		relay='''
				<xml>
				<ToUserName><![CDATA[%s]]></ToUserName>
				<FromUserName><![CDATA[%s]]></FromUserName>
				<CreateTime>%s</CreateTime>
				<MsgType><![CDATA[text]]></MsgType>
				<Content><![CDATA[%s]]></Content>
				<FuncFlag>0<.FuncFlog>
				</xml>
			'''
		if xml_rec.find('MsgType').text =='text':
			if Content.lower()=='笑话':
				content=xiaohua()

			elif '天气' in Content.lower():
				city=Content.replace('-天气','')
				if city:
					content=tianqi(city)
				else:
					content='请输入查询地址(例：湖北武汉-天气)'
			else:
				content=fanyi(Content)

		else:
			Content='暂不支持非文本格式'

		response=make_response(relay%(FromUserName,ToUserName,str(int(time.time())),content))
		response.content_type='application/xml'
		return response
#if __name__=='__main__':
#	app.run()