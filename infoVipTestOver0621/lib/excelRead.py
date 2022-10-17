# 有数据
# 2.读取excel里面的数据
import openpyxl

class excelData:
    def getExcel(self,filename):
        # 找工作簿
        workbook=openpyxl.load_workbook(filename)
        # 表单  指定表单
        sheet=workbook['Sheet1']
        # 拿里面的数据  循环数据
        rows_sheet=sheet.iter_rows()
        # print(rows_sheet)
        list2=[]
        for item in rows_sheet:
            # print(item)
            if item[0].value=='id':
                continue
            # print(item)
            # 这些值在元祖里面的值，放在列表  4个学员 散的 拿出来的数据 会给别的文件用
            # 测试  测试用例 一个文件夹  测试数据  4个学员 给他们
            # 在定义一个空列表 班级  装了4个学员 只要拿到班级 拿到所有的学员
            # list2放在循环里面和放在循环外面有区别的  要整个循环结束之后 拿到所有学员
            # 之后才把他们一起放到列表中去
            # 循环里面  循环第一次 列表有数据  循环第二遍 又重新创建一个列表
            # 循环体结束了 代表整个循环结束了
            list1=[]
            for col in item:
                list1.append(col.value)
            # print(list1)
            list2.append(list1)
        # print(list2)
        return list2

# 把excel里面所有的值都拿出来了  为了后面好使用  封装起来
# 实例化类  方法  多断点 看一下数据是怎么放置进去列表中
# if __name__ == '__main__':
#     a=excelData().getExcel('../data/process.xlsx')
#     print(a)

# 1.已经把excel里面的数据拿到了
# 2.测试数据 测试登录  测试用例 正常情况 异常情况
