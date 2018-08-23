import json


def DictData(self):
    dict_data = self.json()
    return dict_data['data']
    # 将抓取后的数据返回为一个字典包，并去掉开头的data

class WeatherData():

    def __init__(self):
        pass

    def get_yesterday(self):
        return self['yesterday']

    def get_forecast(self):
        return self['forecast']

    def get_date(self):
        #获取日期
        #这里日期没有显示年月
        #为了避免年底或月底时日期出错，不能简单的用日期叠加，而是datetime模块的日期增加函数
        #在这里应将datetime模块结果与天气接口的结果校验，相同后再采用datetime的结果
        #挖个坑，回头2.0版本再加
        revised_date_list = self['date'].split('日')
        revised_date_list.insert(1, '日')
        del revised_date_list[2]
        revised_date = ''.join(revised_date_list)
        return revised_date

    def get_day_in_week(self):
        revised_date_list = self['date'].split('日')
        return revised_date_list[1]


    def get_high(self):
        #获取最高温
        high = self['high']
        return high[3:6]

    def get_fx(self):
        #得到昨天的风向
        return self['fx']

    def get_low(self):
        #得到昨天的低温
        low = self['low']
        return low[3:6]

    def get_fl(self):
        #得到昨天的风力
        fl = self['fl']
        return fl[10:12]

    def get_type(self):
        #得到天气类型
        return  self['type']

    def get_city(self):
        #得到城市名称
        return self['city']

    def get_aqi(self):
        #得到空气质量指数
        return self['aqi']

    def get_fengli(self):
        #得到预报中的风力
        fengli = self['fengli']
        return fengli[10:12]

    def get_fengxiang(self):
        #得到预报的风向
        return self['fengxiang']

    def get_feelingtem(self):
        #获得体感温度
        #这个函数在1.0里没有用过
        return self['wendu']

    #-----------------------下面是直接调用的函数----------------------------------

    def yesterday_weather_list(self):
        origin_dict = WeatherData.get_yesterday(self)
        list = []
        #顺序：日期，天气，最高温度，最低温度，风向，风速
        list.append(WeatherData.get_date(origin_dict))
        list.append(WeatherData.get_day_in_week(origin_dict))
        list.append(WeatherData.get_type(origin_dict))
        list.append(WeatherData.get_high(origin_dict))
        list.append(WeatherData.get_low(origin_dict))
        list.append(WeatherData.get_fx(origin_dict))
        list.append(WeatherData.get_fl(origin_dict))
        #list.append(WeatherData.get_city(origin_dict))
        #list.append(WeatherData.get_aqi(origin_dict)) 昨天的AQI没有必要
        #将含有所有信息的list返回
        return list

    def forecast_weather_list(self,date):
        #天气预报
        origin_dict = WeatherData.get_forecast(self)
        origin_dict = origin_dict[date]
        list = []
        # 顺序：日期，天气，最高温度，最低温度，风向，风速
        list.append(WeatherData.get_date(origin_dict))
        list.append(WeatherData.get_day_in_week(origin_dict))
        list.append(WeatherData.get_type(origin_dict))
        list.append(WeatherData.get_high(origin_dict))
        list.append(WeatherData.get_low(origin_dict))
        list.append(WeatherData.get_fengxiang(origin_dict))
        list.append(WeatherData.get_fengli(origin_dict))
        return list







