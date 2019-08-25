from selenium import webdriver  # 从selenium导入webdriver
import os
import pickle
BASE_PATH = os.path.abspath(os.path.dirname(__file__))
wd = webdriver.Chrome(
    os.path.join(BASE_PATH, 'chromedriver.exe'))  # Optional argument, if not specified will search path.
url = 'https://www.baidu.com/'
wd.get(url)
readPath = open('C:\\Users\\mly\\Desktop\\web自动化\\cookies.txt', 'rb')
BDCookies = pickle.load(readPath)
for cookie in BDCookies:
    wd.add_cookie({
        "domain": ".baidu.com",
        "name": cookie,
        "value": BDCookies[cookie],
        "path": '/',
        "expires": None
    })

wd.get("https://www.baidu.com")




