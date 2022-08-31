from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
search  = driver.find_element_by_id('kw')
search.send_keys('测试')
