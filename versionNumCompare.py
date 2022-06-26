from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException 
from time import sleep
import logging

def wait(driver,locator,waitTime=10):
    try:
            element = WebDriverWait(driver, waitTime).until(EC.presence_of_element_located((By.XPATH, locator)))
    except TimeoutException as exception:
            msg = "Page element locator %s not found or is not visible after %s seconds"
            logging.error(msg, locator, waitTime)
    return

options = webdriver.ChromeOptions()
options.add_argument('ignore-certificate-errors')
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get('https://play.google.com/store/apps/details?id=com.bitoex.bitoproapp') 
aboutBtnXpath="//h2[text()='關於這個應用程式']/../../..//i"
wait(driver,aboutBtnXpath) 
aboutBtn = driver.find_element_by_xpath(aboutBtnXpath) 
aboutBtn.click()
popWindowsVerifyXpath = "//div[contains(text(),'關於這個應用程式')]"
wait(driver,popWindowsVerifyXpath) 
appVersionNumXpath = "//div[text()='版本']/../div[2]"
sleep(1) 
wait(driver,appVersionNumXpath) 
getAndroidVerNum=driver.find_element_by_xpath(appVersionNumXpath).text

driver.execute_script('''window.open("https://apps.apple.com/tw/app/bitopro/id1393007496");''')
driver.switch_to.window(driver.window_handles[-1])
appVersionNumXpath="//p[contains(@class,'whats-new__latest__version')]"
getiOSVerNum=driver.find_element_by_xpath(appVersionNumXpath).text.split(" ")[1]
if(getAndroidVerNum == getiOSVerNum):
	print("APP Version Num \n\t Android Play Store : %s ,\n\t iOS Apple Store : %s \nBoth versions are the same" % (getAndroidVerNum , getiOSVerNum))
else:
	print("APP Version Num \n\t Android Play Store : %s ,\n\t iOS Apple Store : %s \nBoth have different version numbers" % (getAndroidVerNum , getiOSVerNum))
driver.quit()
	
	 