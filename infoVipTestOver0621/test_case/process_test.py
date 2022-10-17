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
    @pytest.mark.parametrize('case',excelData().getExcel('../data/process.xlsx'))
    def test_commanapi(self,case):
        id=case[0]
        url=case[1]
        body=case[2]
        headers=case[3]
        method=case[4]
        param_type=case[5]
        expect=case[6]
        # print('wwwwwwwwww',case)
        httpclient=HttpClient()
        # 发送请求 传参 参数从哪里来？excel里面拿？
        # 我们要的参数已经拿到了 做接口测试
        # method,url,param_type=None,data=None,headers=None,**kwargs
        # 发送请求  发送失败 怎么办？打个断点  没问题 发送请求看一下
        # 用例是写对了 用户信息有没有问题
        # 问题在里面？ 问题 获取个人信息
        # 请求头 是字符串 我根本没有接受头部内容
        common=httpclient(method=method,url=url,param_type=param_type,data=body,headers=headers)
        # 打印结果  4个接口都获得了结果  数据类型  不清楚为什么会出现问题  字符串和字典
        # 可不可以把结果写回到excel里面去
        # 登录走到这里来了  预期结果和实际结果不一致
        # 第一条用例是没有问题  第二条用例  返回来的结果 不是我想要的 用户信息不正确
        # 发送请求有问题
        print(common.json())
        dict_expect=eval(expect)
        try:
            assert dict_expect==common.json()
            rel='用例成功'
        except Exception as e:
            rel='用例失败'

        workbook=openpyxl.load_workbook('../data/process.xlsx')
        sheet=workbook['Sheet1']
        # 数据写进去
        sheet.cell(id+1,8).value=rel
        workbook.save('../data/process.xlsx')

if __name__ == '__main__':
    pytest.main(['-sv','process_test.py'])

# 登录测试测试完成了 测试报告 生成测试报告
# 代码  要的数据类型
# 有兴趣 excel动态的参数获取
# 思路：
# 1.接口响应返回来的值，保存起来 变量中  所有数据的变量
# 2.从excel  麻烦一点  在标记一下 你要去的值 uservar  jsonpath取$..msg

# 有问题的同学下课问我



