from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#launching the browser
browser=webdriver.Firefox()
browser.maximize_window()
browser.get('https://www.google.com/')

try:
    element = WebDriverWait(browser, 100).until(
        EC.presence_of_element_located((By.XPATH, "//a[@title='Google apps']"))
    )
finally:
    browser.find_element(By.XPATH, '//a[@title="Google apps"]').click()

try:
    element = WebDriverWait(browser, 100).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="gb36"]'))
    )
finally:
    browser.find_element(By.XPATH, '//*[@id="gb36"]').click()

assert "YouTube" in browser.title
assert "youtube" in browser.current_url

#closing
browser.close()
browser.quit()
browser.stop_client()