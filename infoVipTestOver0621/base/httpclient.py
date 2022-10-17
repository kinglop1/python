# 专门封装getpost请求方式
import allure
import requests


class HttpClient:
    # 只要用post,get请求方式 就创建会话
    def __init__(self):
        self.session=requests.Session()

    # 发送请求  请求方式，接口地址 ，接口参数类型，接口数据，头部信息,q其他的信息
    # 判断 你要发送的是请求方式 如果get post
    # post请求参数类型 json data
    @allure.step('发送{method}请求')
    def send_request(self,method,url,param_type=None,data=None,headers=None,**kwargs):
        # 请求方式转成大写
        method=method.upper()
        # print(method)
        param_type=param_type.upper()
        # 请求头是字符串类型 改成字典类型
        headers=eval(headers) if headers is not None else headers

        if method=='GET':
            if param_type=='url':
                requestUrl = '%s%s'%(url, "" if data is None else data)
                response=self.session.request(method=method,url=requestUrl,headers=headers,**kwargs)
            else:
                response = self.session.request(method=method, url=url,params_type=data,headers=headers, **kwargs)
        elif method=='POST':
            if param_type=='FORM':
                response=self.session.request(method=method,url=url,data=data,headers=headers,**kwargs)
            else:
                requestData=eval(data)
                response=self.session.request(method=method,url=url,json=requestData,headers=headers,**kwargs)
        elif method=='DELETE':
            if param_type == 'FORM':
                response = self.session.request(method=method, url=url, data=data, **kwargs)
            else:
                response = self.session.request(method=method, url=url, json=data, **kwargs)
        elif method=='PUT':
            if param_type == 'FORM':
                response = self.session.request(method=method, url=url, data=data, **kwargs)
            else:
                response = self.session.request(method=method, url=url, json=data, **kwargs)
        else:
            raise ValueError
        return response

    # 魔法方法  send_request 实例化类.方法
    # 实例化类 HttpClient().send_request()
    # a=HttpClient()  hearders本来有值 走了一遍 就没值
    def __call__(self, method,url,param_type,data=None,headers=None,**kwargs):
        return self.send_request(method,url,param_type,data,headers=headers,**kwargs)

    def close_session(self):
        self.session.close()
