# 这是一个通过人工干预辅助机器登录，操作speexx刷视频的脚本 （开发者：胡时舟）
from selenium import webdriver
import time
import pickle
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
repeat_time = 20
repeat_count = 0  # 重复次数
length_of_video = 190  # 请手动输入今天视频的时长（秒为单位）
driver = webdriver.Chrome()
driver.get('https://portal.speexx.cn/login')
time.sleep(50)
pickle.dump(driver.get_cookies(), open('cookie.pkl', 'wb'))

driver.get('https://portal.speexx.cn/login')
cookies = pickle.load(open('cookie.pkl', 'rb'))
for cookie in cookies:
    driver.add_cookie(cookie)
driver.get('https://portal.speexx.cn/login')
ActionChains(driver).move_to_element(driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div[3]/div[1]/a')).click().perform()
while repeat_count < repeat_time:
    ActionChains(driver).move_to_element(driver.find_element(By.XPATH, '//*[@id="videoContent"]')).click().perform()
    time.sleep(length_of_video)
    time.sleep(1)
    repeat_count += 1

