import pandas as pd
import time
from random import randint
import datetime
# 載入selenium相關模組
from selenium import webdriver

from selenium.webdriver.common.by import By # By是selenium裏面的一個類別。
from selenium.webdriver.chrome.options import Options
#建立Driver物件實體，用程式操作瀏覽器運作
driver = webdriver.Chrome()

       
# 如果想要在vs code這裏看網頁的原始碼，則
# print(driver.page_source) #取得網頁的原始碼 
# for url_link in url:
# target_num_result = 100 # our target product message is 100
#below code is remove the advertising


#below code is download all product in every page
# while len(Product_result1) < target_num_result:
    # product_elements = driver.find_elements(By.XPATH, '//div[@class="grid-view-item product-card"]') 
#     for product in product_elements:
#         Product_result1.append(product.text)
#     print(len(Product_result1))

#     if len(Product_result1) >=target_num_result:
#         break
#     print('----')

product_url = []
product_title = []#-------230805
vendor_name = []#-------230805
regular_price = []#-------230805 empty set
sale_price = []#-------230805
promotion = []   #-------230807 
product_in_stock = [] #-------230808
product_out_stock = [] #-------230808
product_page = []
Product_image = []


# urls = [
#     "https://babycentral.com.hk/zh/collections/skincare-1848435913",
#     "https://babycentral.com.hk/zh/collections/snacks",
# ]
# for url in urls:
for i in range(5):
    page = 1+i
    # 去到你想要的網頁
    # url = "https://babycentral.com.hk/zh/collections/skincare-1848435913"
    url="https://babycentral.com.hk/zh/collections/snacks"
    # url= "https://babycentral.com.hk/zh/collections/carriers-and-wraps"
    # url = "https://babycentral.com.hk/zh/collections/baby-formula"
    # url = "https://babycentral.com.hk/zh/collections/strollers"
    # url = "https://babycentral.com.hk/zh/collections/diapers-200893269"
    # url = "https://babycentral.com.hk/zh_collections/gear"
    # url = "https://babycentral.com.hk/zh/collections/maternity"
    # url = "https://babycentral.com.hk/zh/collections/post-partum-care"

    try:
        adv_button1= driver.find_element(By.XPATH, '//button[@class="needsclick klaviyo-close-form kl-private-reset-css-Xuajs1"]')
        adv_button1.click()
    except:
        pass

    # try:
    #     zh_button1= driver.find_element(By.XPATH, '//div[@class=" language-btn "]')
    #     zh_button1.click()
    # except:
    #     pass


    if page > 1:
        url +="?bbchk_products%5Bpage%5D=" + str(page)
    
    driver.get(url)

    # try:
    #     zh_button1= driver.find_element(By.XPATH, '//div[@class=" language-btn "]')
    #     zh_button1.click()
    # except:
    #     pass

    #gett url
    product_elements = driver.find_elements(By.XPATH, '//div[@class="grid-view-item product-card"]') 
    for pageurl in product_elements:
        a_page_url = pageurl.find_elements(By.TAG_NAME, 'a') 
        for j in a_page_url:
            product_url.append(j.get_attribute('href'))

    #find out price title-------230805
    product_titles = driver.find_elements(By.XPATH, '//div[@class="h4 grid-view-item__title product-card__title"]')
    for product_name in product_titles: #for 裏面的名字不能跟[]重複
        title_text = product_name.text #將内容轉換成text，即係可顯示的資料。
        product_title.append(title_text) #這個步驟是把data放進product_title = []裏面        

    # print(len(product_title))
    # print(product_title)

    # find out vendor_name-------230805
    vendor_names = driver.find_elements(By.XPATH, '//div[@class="price__vendor price__vendor--listing"]')
    for v_name in vendor_names:
        vendor_text = v_name.text.replace('Vendor\n', '')  #將内容轉換成text，即係可顯示的資料。
        vendor_name.append(vendor_text)  #這個步驟是把data放進vendor_name = []裏面
# print(vendor_name)
# print(len(vendor_name))

    # find out regular_price-------230805
    regular_prices = driver.find_elements(By.XPATH, '//span[@class="price-item price-item--regular"]')
    for regular_price_list in regular_prices:
        regular_p_text = regular_price_list.text #將内容轉換成text，即係可顯示的資料。
        number_a = len(regular_p_text) # we need to len the a first, 
        if number_a > 0: #if the result is >0, 
            regular_price.append(regular_p_text) # then append the info 
        else: # if can not work, this is mean the len a is < 0, 
            regular_price.append('NA') # then append NA as a info
# print(regular_p_text)
# print(len(regular_p_text))
# print('--------')
# print(len(regular_price))

    # find out sale_price-------230807
    sale_prices = driver.find_elements(By.XPATH, '//span[@class="price-item price-item--sale"]')
    for sale_price_list in sale_prices:
        sale_p_text = sale_price_list.text
        number_b = len(sale_p_text)
        if number_b > 0:
            sale_price.append(sale_p_text)
        else:
            sale_price.append('NA')
# print(sale_p_text)
# print(len(sale_p_text))
# print(len(sale_price))

    # find out promotion-------230808
    for promotion_list in product_elements:
        try:
            promotion.append(promotion_list.find_element(By.CLASS_NAME, 'price__bff').text)
        except:
            promotion.append('NA')   
# print(len(promotion))

    # find out product_in_stock-------230808
    for product_is_list in product_elements:
        # product_out_stocks = product_is_list.find_element(By.CLASS_NAME, 'shipping-grey')
        # product_os_text = product_out_stocks.text
        try:
            product_in_stock.append(product_is_list.find_element(By.CLASS_NAME, 'readytoship').text)
        except:
            product_in_stock.append('NA')   
# print(len(product_in_stock))

    # find out product_out_stock-------230808
    for product_os_list in product_elements:
        try:
            product_out_stock.append(product_os_list.find_element(By.CLASS_NAME, 'shipping-grey').text)
        except:
            product_out_stock.append('NA')   
# print(len(product_out_stock))


    #find out product image
    product_elements_ima =  driver.find_elements(By.XPATH, '//div[@style="text-align:center;"]')
    for product_im in product_elements_ima:
        product_im_image = product_im.find_elements(By.TAG_NAME, 'img')
        for k in product_im_image:
            Product_image.append(k.get_attribute('data-src'))
# print(Product_image)
# print(len(Product_image))

    # get 每個產品的 url
    for geturl in product_elements:
        # print(geturl)
        # print('------')
        # print(result.text.split('\n'))
        a_tags_list = geturl.find_elements(By.TAG_NAME, 'a') 
        for a_tag in a_tags_list:
            product_page = a_tag.get_attribute('href')
    # print(len(product_page))

#  建立一個dataframe
df = pd.DataFrame({
    'product_title':product_title, 
    'vendor_name':vendor_name, 
    'regular_price':regular_price, 
    'sale_price':sale_price, 
    'promotion':promotion,
    'product_in_stock':product_in_stock, 
    'product_out_stock':product_out_stock,
    'Product_image':Product_image,
    'product_page':product_page})
print(df)

# 獲取當前日期和時間
current_datetime = datetime.datetime.now()

# 格式化日期和時間字符串
datetime_string = current_datetime.strftime("%Y%m%d_%H%M")

# file名字
file_name = f'Baby Central_snacks_eng_{datetime_string}.csv'

df.to_csv(
        file_name, # 檔案名稱
        encoding = 'utf-8-sig', # 編碼
        index=False # 是否保留index
        )