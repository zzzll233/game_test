import openpyxl
import csv

'''
读取策划 Excel，实现一键配置校验
'''

# 打开Excel文件
workbook = openpyxl.load_workbook('monsters.xlsx')
# 假设要检验的工作表是第一个工作表
sheet = workbook.active  # 获取当前活动的工作表

'''读取表头（假设表头在第一行）,建立一个字典来存储表头和对应的列索引''' 
# 读取并过滤掉空表头，剔除多余的空列
raw_headers = [cell.value for cell in sheet[1]]  # 获取第一行的表头信息
# 只保留列名不为空的列,保留索引，用索引取数据,防止出现空列导致数据错位
valid_headers = [idx for idx, i in enumerate(raw_headers) if i is not None] # 获取非空表头的索引
# 根据有效表头索引获取对应的表头名称
headers = [raw_headers[idx] for idx in valid_headers]  # 获取有效表头名称  

# 检查表头是否重复
if len(headers) != len(set(headers)):
    raise ValueError("表头存在重复项，请检查Excel文件。")
print(f"表头信息:{headers}")


# 逐行读取数据，转换成字典列表
monsters_data = [] 
format_errors = []  # 用于存储格式错误的行信息

for row_idx, row in enumerate(sheet.iter_rows(min_row=2, values_only=True), start=2): # 从第二行开始读取数据
   
    # 只取有效列对应的单元格数据
    clean_row = [row[i] for i in valid_headers]

    # 检查列数是否匹配（理论上这里应该已经相等，但可以保留）
    if len(clean_row) != len(headers):
        format_errors.append(f"第{row_idx}行数据列数与表头不一致")
        continue

    # 检查每行数据是否有空值
    has_empty = False
    for col_idx, cell in enumerate(clean_row):  # 判断该行数据组，有没有空数据
        if cell is None:
            format_errors.append(f"第{row_idx}行，第{col_idx+1}列（{headers[col_idx]}）为空")
            has_empty = True
    if has_empty:  # 若某行某列存在空数据，则放入格式错误的列表中，不进入monsters_data中，进行数据检验
        continue
       
    monster_dict = dict(zip(headers, clean_row)) # 将表头和每行数据对应起来，形成字典，每行数据做一个none值的校验
    monsters_data.append(monster_dict) # 将每行数据放入字典列表中

# 输出format_errors 存储格式错误的行信息
for error in format_errors:
    print(error)

# 校验获得到的字典列表monsters_data
error_details = []

for monster in monsters_data:
    errors = []
    if monster["血量"] <= 0:
       errors.append(f"血量异常{monster['血量']}")
    if monster["攻击力"] <= 0:
        errors.append(f"攻击力异常{monster['攻击力']}")
    if monster["等级"] <= 0:
        errors.append(f"等级异常{monster['等级']}")

    if errors:
        error_details.append({"name": monster["名称"], "errors": errors})
        
if not error_details:
    print("所有怪物配置正常。")
else:
    print("异常怪物详情：")
    for detail in error_details:
        print(f"怪物名称: {detail['name']}, 异常信息: {', '.join(detail['errors'])}")   

# 导出csv文件报告
with open("check_open.csv", "w", newline="",encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["类型", "行号", "列号", "详细信息"])
    for error in format_errors:
        writer.writerow(["格式错误", "", "", error])
    for detail in error_details:
        for err in detail["errors"]:
            writer.writerow(["数值异常", detail["name"], "", err])

# 最终状态码（可选：如果有异常可让脚本退出码非0，方便集成到CI）
if format_errors or error_details:
    exit(1)  # 有错误时返回非0，方便自动化流程判断
