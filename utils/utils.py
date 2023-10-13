import urllib
import urllib.request as request
import urllib.error as error
import json

class API():
    #defined a class for invoking the required interface

    def news(self,area):
        #this interface is used to get news information
        api_url = 'http://apis.juhe.cn/fapigx/areanews/query'#get API_url
        params_dict = {
            "areaname":area,#province name
            "key": "957ca23f2e2ecd76628d4481d7c094b7",#API interface request key
        }
        #enter the request parameter:key,areaname
        params = urllib.parse.urlencode(params_dict)
        req = request.Request(api_url, params.encode())
        response = request.urlopen(req)
        content = response.read()
        #receive the return parameters
        if content:
                result = json.loads(content)
                error_code = result['error_code']
                #load the return parameters using json
                if (error_code == 0):
                    return result['result']
                    #return a list
                else:
                    return []
                    #return a not valid code
        else:
            return []
            #return a not valid code
        
    def scenic_spot(self,cty):
        #this interface is used to get scenic spot
        #usage is the same as the previous function
        api_url = 'http://apis.juhe.cn/fapigx/scenic/query'
        params_dict = {
            "city":cty, #city name
            "key": "7c89e50cc8677385906b660acc674c2e",#API interface request key
            "word":"none", #required input
            "num":15,#the number of the spots
        }
        params = urllib.parse.urlencode(params_dict)
        req = request.Request(api_url, params.encode())
        response = request.urlopen(req)
        content = response.read()
        if content:
                result = json.loads(content)
                error_code = result['error_code']
                if (error_code == 0):
                    return result['result']
                else:
                    return []
        else:
                return []
        
    def weather(self,cty):
        #this interface is used to get weather
        #usage is the same as the previous function
        api_url = 'http://apis.juhe.cn/simpleWeather/query'
        params_dict = {
            "city": cty,  
            "key": "f3ad7e5805ab82e60a1a688223cb6473", 
        }
        params = urllib.parse.urlencode(params_dict)
        req = request.Request(api_url, params.encode())
        response = request.urlopen(req)
        content = response.read()
        if content:
            result = json.loads(content)
            error_code = result['error_code']
            if (error_code == 0):
                #to get the temperature and else in the list
                temperature = result['result']['realtime']['temperature']
                humidity = result['result']['realtime']['humidity']
                info = result['result']['realtime']['info']
                direct = result['result']['realtime']['direct']
                power = result['result']['realtime']['power'] 
                aqi = result['result']['realtime']['aqi']
                return temperature,humidity,info,direct,power,aqi
            else:
                return 999,999,999,999,999,999 #return a not valid code
        else:
            return 999,999,999,999,999,999 #return a not valid code