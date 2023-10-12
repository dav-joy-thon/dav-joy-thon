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
        
    
