# pip install selenium
# pip install beautifulsoup4
import selenium
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-logging']) # 불필요한 에러 메시지 삭제
driver = webdriver.Chrome(options=options)

# a = driver.get('https://cheongwon.go.kr/portal/petition/open/view?pageIndex=1&searchType=2&searchKeyword=&type=card')
# time.sleep(3)

result_list=[]

for i in range(1, 11):
    driver.get("https://cheongwon.go.kr/portal/petition/open/view?pageIndex="+str(i)+"&searchType=2&searchKeyword=&type=card")
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    sub = driver.find_elements(By.CSS_SELECTOR, value='#lay-content > div > div > div.open_box > ul.list_card > li > a > span.subject')
    
    for subs in sub:
        # print(subs.text.strip())
        result_list.append(subs.text)
    time.sleep(3)

driver.close()

# 필요할 때마다 불러오기는 번거로우니 엑셀에 저장.
from openpyxl import Workbook
# pip install openpyxl

write_workbook = Workbook()
write_cell = write_workbook.active

for i in range(1, len(result_list)+1):
    write_cell.cell(i,1,result_list[i-1])

write_workbook.save("cheong.xlsx")