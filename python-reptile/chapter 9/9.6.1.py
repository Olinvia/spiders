from selenium import webdriver
import json, time
# 百度用户登录并保存登录Cookies
path = 'D:\\Use\\gitcode\\spiders\\python-reptile\\chromedriver.exe'
driver = webdriver.Chrome(executable_path=path)
driver.get("https://www.baidu.com/")

driver.find_element_by_id('s-top-loginbtn').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__changeSmsCodeItem"]').click()

# 设置用户的账号和密码
driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__smsPhone"]').send_keys('XXXX')
time.sleep(3)
"""
try:
    verifyCode = driver.find_element_by_name('verifyCode')
    code_number = input('请输入图片验证码：')
    verifyCode.send_keys(str(code_number))
except: pass
"""

try:
    driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__smsTimer"]').click()
    code_photo = input('请输入短信验证码：')
    driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__smsVerifyCode"]').send_keys(str(code_photo))
    driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__smsIsAgree"]').click()
    driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__smsSubmit"]').click()
    time.sleep(3)
except: pass

cookies = driver.get_cookies()
f1 = open('cookie.txt', 'w')
f1.write(json.dumps(cookies))
f1.close()