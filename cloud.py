from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time

with open("./store.txt") as f:
    temp = f.read()
    if temp == str(time.localtime(time.time()).tm_mday):
        print(time.localtime(time.time()).tm_mday)
        exit()
    f.close()

chrome_options = Options()
chrome_options.add_argument("--headless")
base_url = "https://portal.pku.edu.cn/portal2017/#/bizCenter"
driver = webdriver.Chrome(
    executable_path=(r'.\venv\chromedriver.exe'),
    chrome_options=chrome_options)

start_time = time.time()
print('this is start_time ', start_time)

# 这里
img_path="C://Users//lenovo//Desktop//cloudfight"

def get_url():
    try:
        print(base_url)
        driver.get(base_url)
        time.sleep(1.5)
        user_name = driver.find_element_by_css_selector('#user_name')
        # 这里
        user_name.send_keys('2001210564')
        time.sleep(0.5)
        password = driver.find_element_by_id('password')
        # 这里
        password.send_keys('cky15115930101')
        time.sleep(0.5)
        button = driver.find_element_by_id('logon_button')
        button.click()
        time.sleep(5)
        t=driver.find_element_by_xpath("//*[text()='我知道了']")
        t.click()
        time.sleep(1)
        fight = driver.find_element_by_id('epidemic')
        fight.click()
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[-1])
        # driver.save_screenshot("1.png")
        label = driver.find_element_by_xpath(
            '//label[@for="sfczzz"]/following-sibling::div')
        label.find_element_by_xpath('./label[2]').click()
        health = driver.find_element_by_xpath(
            '//label[@for="yqzd"]/following-sibling::div')
        health.click()
        time.sleep(3)
        driver.find_element_by_xpath(
            '//body/div[last()]/div[1]/div[1]/ul/li[1]').click()
        driver.save_screenshot(img_path+'cloudfight1.png')
        driver.find_element_by_css_selector('.el-button--primary').click()
        time.sleep(1)
        driver.save_screenshot(img_path+'cloudfight2.png')

        with open("./store.txt", 'w') as f:
            f.write(str(time.localtime(time.time()).tm_mday))
            f.close()        

    except:
        driver.save_screenshot(img_path+'fail.png')
        print("失败")


get_url()

driver.quit()
end_time = time.time()
print('this is end_time ', end_time)
exit()
print('after exit')
