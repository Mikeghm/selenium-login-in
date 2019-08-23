from selenium import webdriver # 从selenium导入webdriver
import time
import os

BASE_PATH = os.path.abspath(os.path.dirname(__file__))

wd = webdriver.Chrome(os.path.join(BASE_PATH, 'chromedriver.exe'))  # Optional argument, if not specified will search path.
url = 'https://www.baidu.com/'
wd.get(url) # 获取百度页面
login = wd.find_elements_by_css_selector('div[id=u1] a[class=lb]')[0]
login.click()
time.sleep(2)
usernamelogin = wd.find_element_by_css_selector('#TANGRAM__PSP_10__footerULoginBtn')
usernamelogin.click()
time.sleep(2)
username = wd.find_element_by_css_selector('#TANGRAM__PSP_10__userName')
username.send_keys('13267116369')
time.sleep(1)
password = wd.find_element_by_css_selector('#TANGRAM__PSP_10__password')
password.send_keys('Mikeghm0506')
time.sleep(1)
login2 = wd.find_element_by_css_selector('#TANGRAM__PSP_10__submit')
login2.click()
time.sleep(1)
sendcode = wd.find_element_by_css_selector('#TANGRAM__39__button_send_mobile')
sendcode.click()
time.sleep(10)

code = input("请输入验证码:")
inputcode = wd.find_element_by_css_selector('#TANGRAM__39__input_vcode')
inputcode.send_keys(code)
time.sleep(1)
confirm = wd.find_element_by_css_selector('#TANGRAM__39__button_submit')
confirm.click()
