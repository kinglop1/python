# 测试excel里面的数据
# 知识点 写这块 比较友好 读取数据做测试
# 测试数据 做登录测试  用什么知识点  pytest/unittest  单元测试框架  自动化里面写用测试用例
# 用代码去写测试用例  测试  unittest/pytest  管理用例 参数化 unittest/pytest
# 从yaml文件中拿到数据 excel文件中拿到数据 惊喜  生成测试报告
# 测试登录 登录数据拿到  拿到数据
# 拿到登录数据 发送请求 写过一次封装请求
import allure
import openpyxl
import pytest

from base.httpclient import HttpClient
from lib.excelRead import excelData


class TestCase:
    @pytest.mark.parametrize('case',excelData().getExcel('../data/login1.xlsx'))
    def test_commanapi(self,case):
        # 以用例中的模块作为测试报告的模块名
        if case[7] is not None:
            allure.dynamic.feature(case[7])
        if case[8] is not None:
            allure.dynamic.story(case[8])
        if case[9] is not None:
            allure.dynamic.title(case[9])
        if case[10] is not None:
            allure.dynamic.description(case[10])
        if case[11] is not None:
            allure.dynamic.severity(case[11])
        id=case[0]
        url=case[1]
        body=case[2]
        method=case[3]
        param_type=case[4]
        expect=case[5]
        # print('wwwwwwwwww',case)
        httpclient=HttpClient()
        # 发送请求 传参 参数从哪里来？excel里面拿？
        # 我们要的参数已经拿到了 做接口测试
        # method,url,param_type=None,data=None,headers=None,**kwargs
        # 发送请求  发送失败 怎么办？打个断点  没问题 发送请求看一下
        common=httpclient(method=method,url=url,param_type=param_type,data=body)
        # 打印结果  4个接口都获得了结果  数据类型  不清楚为什么会出现问题  字符串和字典
        # 可不可以把结果写回到excel里面去
        print(common.json())
        dict_expect=eval(expect)
        try:
            assert dict_expect==common.json()
            rel='用例成功'
        except Exception as e:
            rel='用例失败'

        workbook=openpyxl.load_workbook('./data/login1.xlsx')
        sheet=workbook['Sheet1']
        # 数据写进去
        sheet.cell(id+1,7).value=rel
        workbook.save('./data/login1.xlsx')

if __name__ == '__main__':
    pytest.main(['-sv','login_test.py'])

# 登录测试测试完成了 测试报告 生成测试报告





