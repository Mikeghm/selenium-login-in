from selenium import webdriver  # 从selenium导入webdriver
import time
import os
import pickle
BASE_PATH = os.path.abspath(os.path.dirname(__file__))
wd = webdriver.Chrome(
    os.path.join(BASE_PATH, 'chromedriver.exe'))  # Optional argument, if not specified will search path.
url = 'https://www.baidu.com/'
wd.get(url)
time.sleep(30)  # 获取百度页面
BaiduCookies = wd.get_cookies()
wd.quit()
cookies = {}
for item in BaiduCookies:
    cookies[item['name']] = item['value']
outputPath = open('C:\\Users\\mly\\Desktop\\web自动化\\cookies.txt', 'wb')
pickle.dump(cookies, outputPath)
outputPath.close()
print(cookies)


