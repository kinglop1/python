
import json

import jsonpath


# 这部分是动态取接口的值，有兴趣的可以看下
depend={}

class operatorConvert:
    def convertBody(self, body):
        listsvar = body.split('$')
        # print(listsvar)
        # 循环列表变量获得参数值
        num=0
        for strValue in listsvar:
            # print(strValue)
        # 并不是要所有的值 只要单个值  如果是循环出来是单数就把值给到newstrValue
            if num%2==1:
                newstrValue=strValue
                # print(newstrValue)
                # 在新值里面找到 变量名 通过变量名就能拿到全局变量的值
                strvar=newstrValue[:newstrValue.find('.')]
                allvalue=depend[strvar]
                # print(allvalue)
                # 在新值里面找到 后缀表达式  因为全局变量里面没值所以里面没数据
                jsonpathValue=newstrValue[newstrValue.find('.')+1:]
                # print(jsonpathValue)
                allvalue2 = json.loads(allvalue)
                # 拿到allvalue  通过表达式取出值
                varchuck=jsonpath.jsonpath(allvalue2,expr='$.'+jsonpathValue)
                # print(varchuck)
                listsvar[num] = str(varchuck[0])
                # print(listsvar[num])
            num = num + 1
        strsplitvar=''.join(listsvar)
        # print(strsplitvar)
        return strsplitvar
# operatorConvert().convertBody(body)

