import pandas as pd
import glob
import os

#第一步：把所有產品的csv集合成一個csv
#前面的r是因爲要求反斜杠
# C:\Users\Gemcy\Desktop\JDE7_Gemcy\selenium\ztore_0814是文件所在路徑。
#使用通配符(*.csv)在当前目录中查找所有以.csv为扩展名的文件的代码行。
csv_files = glob.glob(r'C:\Users\Gemcy\Desktop\JDE7_Gemcy\selenium\ztore_0816\*.csv')

merged_data = pd.DataFrame()

for file in csv_files:
    if os.path.isfile(file):  
        df = pd.read_csv(file)
        merged_data = pd.concat([merged_data, df], ignore_index=True)

# merged_data = merged_data.drop("product_comments", axis=1)  # 使用drop()函数删除了名为"product_comments"的列。axis=1表示删除列，而不是行。
merged_data = merged_data.fillna("null")  #使用fillna()函数将DataFrame中的空格部分填充为"null"。如果表格沒有空格，則不需要用這個code

#前面的r是因爲要求反斜杠
#C:\Users\Gemcy\Desktop\JDE7_Gemcy\selenium\merge是文件所在路徑
#\ztore_0814_merge.csv 是輸出后的文件名
#在to_csv()函数中添加了encoding='utf-8'参数，将输出文件的编码设置为UTF-8。
merged_data.to_csv(r'C:\Users\Gemcy\Desktop\JDE7_Gemcy\selenium\merge\ztore_0816_merge.csv', index=False, encoding='utf-8')  

print('完成')

#--------------------------------------------------------------------

# #第二步：把要分開的columns另存csv
# # input_file = r'C:\Users\Gemcy\Desktop\JDE7_Gemcy\selenium\merge\ztore_0814_merge.csv'  # 输入文件名
# # output_file = r'C:\Users\Gemcy\Desktop\JDE7_Gemcy\selenium\merge\ztore_0814_merge_prod_info.csv'  # 输出文件名
# # selected_columns = ['sources','categories','vendor_name', 'product_title', 'product_original','product_image','every_product_url']  # 要选择的列名称列表

# # input_file = r'C:\Users\Gemcy\Desktop\JDE7_Gemcy\selenium\merge\ztore_0815_merge.csv'  # 输入文件名
# # output_file = r'C:\Users\Gemcy\Desktop\JDE7_Gemcy\selenium\merge\ztore_0815_merge_promo_info.csv'  # 输出文件名
# # selected_columns = ['sources','categories','vendor_name', 'product_title', 'product_original','sale_price','promotion','product_image','every_product_url']  # 要选择的列名称列表

# input_file = r'C:\Users\Gemcy\Desktop\JDE7_Gemcy\selenium\merge\ztore_0814_merge.csv'  # 输入文件名
# output_file = r'C:\Users\Gemcy\Desktop\JDE7_Gemcy\selenium\merge\ztore_0814_merge_prices_info.csv'  # 输出文件名
# selected_columns = ['sources','categories','vendor_name', 'product_title', 'regular_price','sale_price','promotion','every_product_url']  # 要选择的列名称列表

# df = pd.read_csv(input_file) # 读取CSV文件
# selected_df = df[selected_columns] # 选择指定的列
# selected_df.to_csv(output_file, index=False)# 将选择的列保存为新的CSV文件

# print("已将指定的列数据保存到output.csv文件中。")

#--------------------------------------------------------------------

# merged_data.fillna('null')
# product_comments=list(merged_data.to_dict()["product_comments"].values())
# for product_comment in product_comments:
#     for comment_line in product_comment.split("\n"):  
#         print(comment_line)


#******以下code是在現有的csv，如果有空格，則填充null*****
# import csv

# input_file = r"C:\Users\Gemcy\Desktop\JDE7_Gemcy\selenium\merge\merge.csv"  # 输入CSV文件的路径,前面的r是因爲要求反斜杠
# output_file = r"C:\Users\Gemcy\Desktop\JDE7_Gemcy\selenium\merge\merge_null.csv"  # 输出CSV文件的路径,前面的r是因爲要求反斜杠

# # 打开输入和输出文件
# with open(input_file, "r", encoding="utf-8") as file_in, open(output_file, "w", newline="", encoding="utf-8") as file_out: #如果csv本不是UTF-8編碼，而是GBK編碼則用這個code
# # with open(input_file, "r") as file_in, open(output_file, "a", newline="") 如果csv本來就是UTF-8格式，則用這個code
#     reader = csv.reader(file_in)
#     writer = csv.writer(file_out)

#     # 逐行读取输入文件并写入输出文件
#     for row in reader:
#         # 将每个单元格的空格替换为"null"
#         row = ["null" if cell.strip() == "" else cell for cell in row]
#         writer.writerow(row)

# print("空格填充完成。")
#******以上code是在現有的csv，如果有空格，則填充null*****


# import pandas as pd

# df = pd.read_csv('merge/merge2.csv', header=0)
# df = df.fillna(value='null') #識辨空格，然後把空格填null

# print(df)

#df.to_csv('C:/Users/Gemcy/Desktop/JDE7_Gemcy/selenium/merge2.csv', index=False) # 將舊的CSV改成新的CSV，但是舊的CSV還是存在的

