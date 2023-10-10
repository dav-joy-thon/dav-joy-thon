import urllib
import urllib.request as request
import urllib.error as error
import json
def weather():
    cty=input("请输入感兴趣的城市:")
    api_url = 'http://apis.juhe.cn/simpleWeather/query'
    params_dict = {
        "city": cty,  # 城市名称
        "key": "f3ad7e5805ab82e60a1a688223cb6473",  # API接口请求Key
    }
    params = urllib.parse.urlencode(params_dict)
    try:
        req = request.Request(api_url, params.encode())
        response = request.urlopen(req)
        content = response.read()
        if content:
            try:
                result = json.loads(content)
                error_code = result['error_code']
                if (error_code == 0):
                    temperature = result['result']['realtime']['temperature']
                    humidity = result['result']['realtime']['humidity']
                    info = result['result']['realtime']['info']
                    wid = result['result']['realtime']['wid']
                    direct = result['result']['realtime']['direct']
                    power = result['result']['realtime']['power']
                    aqi = result['result']['realtime']['aqi']
                    print("温度：%s\n湿度：%s\n天气：%s\n天气标识：%s\n风向：%s\n风力：%s\n空气质量：%s" % (
                        temperature, humidity, info, wid, direct, power, aqi))
                else:
                    print("请求失败:%s %s" % (result['error_code'], result['reason']))
            except Exception as e:
                print("解析结果异常：%s" % e)
        else:
            # 可能网络异常等问题，无法获取返回内容，请求异常
            print("请求异常")
    except error.HTTPError as err:
        print(err)
    except error.URLError as err:
        # 其他异常
        print(err)
if __name__ == "__main__":
    weather()