from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Ie("D:\\python\\iedriver\\IEDriverServer.exe")
driver.get("http://localhost/GHS_ManagementSystem/Login.aspx")
# assert "AdministrationService Service" in driver.title
elem = driver.find_element_by_name("ctl00$ContentPlaceHolder1$loginControl$UserName")
elem.send_keys("ghssupport")
elem = driver.find_element_by_name("ctl00$ContentPlaceHolder1$loginControl$Password")
elem.send_keys("tesco")
elem.send_keys(Keys.RETURN)

#driver.close()
