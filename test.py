#-*- coding: utf-8 -*
import datetime
weather_data = {'data': {'yesterday': {'date': '22日星期三', 'high': '高温 30℃', 'fx': '北风', 'low': '低温 22℃', 'fl': '<![CDATA[3-4级]]>', 'type': '阴'}, 'city': '临沂', 'forecast': [{'date': '23日星期四', 'high': '高温 30℃', 'fengli': '<![CDATA[4-5级]]>', 'low': '低温 19℃', 'fengxiang': '北风', 'type': '多云'}, {'date': '24日星期五', 'high': '高温 30℃', 'fengli': '<![CDATA[<3级]]>', 'low': '低温 20℃', 'fengxiang': '北风', 'type': '晴'}, {'date': '25日星期六', 'high': '高温 29℃', 'fengli': '<![CDATA[<3级]]>', 'low': '低温 20℃', 'fengxiang': '东风', 'type': '晴'}, {'date': '26日星期天', 'high': '高温 30℃', 'fengli': '<![CDATA[3-4级]]>', 'low': '低温 20℃', 'fengxiang': '东南风', 'type': '多云'}, {'date': '27日星期一', 'high': '高温 29℃', 'fengli': '<![CDATA[3-4级]]>', 'low': '低温 22℃', 'fengxiang': '东北风', 'type': '阴'}], 'ganmao': '各项气象条件适宜，发生感冒机率较低。但请避免长期处于空调房间中，以防感冒。', 'wendu': '28'}, 'status': 1000, 'desc': 'OK'}

#aaa = '<![CDATA[<3级]]>'

list = ['aaa','bbb',222]
list.append(['aaa',22])
print(list)
#print(len(list))

# aaa1 = weather_data['data']
# aaa2 = aaa1['forecast']
# aaa3 = aaa2[1]
# print(aaa3)

# print("aaa\taaaaa\taaa\taaaa\ta")
# print("a\taaa\tab\t1\taaa")

# date = '22日星期三'
# revised = date.split('日')
# revised.insert(1,'日, ')
# print(''.join(revised))

# print(datetime.datetime.now())