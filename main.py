import requests
import Decoding
import os
from city import Citylist

#导入requests爬虫模块，Decoding对天气信息解包模块，以及Citylist这个城市信息类

os.system("title 城市天气查询v1.0")

print("请输入城市名称")
city_name = input(">")
city_selected = Citylist.Get_CityNumber(city_name)
#获取用户想要得到的城市信息

weather_load = {'citykey':city_selected}
weather_data_web = requests.get('http://wthrcdn.etouch.cn/weather_mini',params=weather_load)
#抓取城市天气信息

weather_data = Decoding.DictData(weather_data_web)
#将上面得到的json包转换为字典包

yesterday = Decoding.WeatherData.yesterday_weather_list(weather_data)
today = Decoding.WeatherData.forecast_weather_list(weather_data, 0)
tomorrow = Decoding.WeatherData.forecast_weather_list(weather_data, 1)
dayaftertomorrow = Decoding.WeatherData.forecast_weather_list(weather_data, 2)
dayafter2tomorrow = Decoding.WeatherData.forecast_weather_list(weather_data, 3)
dayafter3tomorrow = Decoding.WeatherData.forecast_weather_list(weather_data, 4)


#将字典包交给Decoding模块里的函数解包

#测试用

# print(dayafter3tomorrow)
#测试用


print_information = ['日期', '天气', '最高温度', '最低温度', '风向', '风速']

print("\t\t\t\t\t\t城市：\t%s\n" %city_name)
# for display_counter in range(0,6):
#     print("%s\t\t%s \t\t%s \t\t%s \t\t%s \t\t%s \t\t%s\n" %(print_information[display_counter], yesterday[display_counter],
#                                                today[display_counter], tomorrow[display_counter],
#                                                dayaftertomorrow[display_counter],
#                                          dayafter2tomorrow[display_counter],
#                                          dayafter3tomorrow[display_counter]
#                                          ))
#由于GUI还不会用，这些数据太多会显示错乱
#先只放昨天今天明天三天的数据吧


for display_counter in range(0,6):
    print("%s\t\t%s\t\t%s\t\t%s\n" %(print_information[display_counter], yesterday[display_counter],
                                               today[display_counter], tomorrow[display_counter]
                                         ))

print("\n\n\n")

for display_counter in range(0,6):
    print("%s\t\t%s\t\t%s\t\t%s\n" %(print_information[display_counter],
                                     dayaftertomorrow[display_counter],
                                     dayafter2tomorrow[display_counter],
                                     dayafter3tomorrow[display_counter]))


input("按回车键结束程序")
