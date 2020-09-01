from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.keys import Keys
import time

webdriver_service = service.Service('operadriver_win64/operadriver')
webdriver_service.start()

driver = webdriver.Remote(webdriver_service.service_url, webdriver.DesiredCapabilities.OPERA)

driver.get('https://nametool.co/hotmail/')

inp = driver.find_element_by_name('usernames')

username = 'gbknonur'

for i in range(1, 1000):
    inp.send_keys(username + str(i).rjust(3, '_'), Keys.RETURN)
    
    time.sleep(2)
    inp.clear()
