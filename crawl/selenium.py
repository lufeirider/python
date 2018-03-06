from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#关闭提示安全提示框
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--disable-infobars")


driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver",chrome_options=chrome_options)
driver.get("https://www.baidu.com/")
elem = driver.find_element_by_name("wd")
elem.send_keys("lufei")
elem.send_keys(Keys.RETURN)