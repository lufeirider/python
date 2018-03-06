from selenium import webdriver

driver = webdriver.PhantomJS()
driver.get("https://www.baidu.com/")
print(driver.page_source)
driver.quit()

