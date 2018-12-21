from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#launching the browser
browser=webdriver.Firefox()
browser.maximize_window()
browser.get('https://www.youtube.com/')

try:
    element = WebDriverWait(browser, 100).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="title-container" and contains(.,"Trending")]/parent::div/following-sibling::div//*[@id="items"]/ytd-grid-video-renderer[1]//a[@id="thumbnail"]'))
    )
finally:
    browser.find_element(By.XPATH, '//*[@id="title-container" and contains(.,"Trending")]/parent::div/following-sibling::div//*[@id="items"]/ytd-grid-video-renderer[1]//a[@id="thumbnail"]').click()

try:
    element = WebDriverWait(browser, 100).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="items"]/ytd-compact-autoplay-renderer//a[@id="thumbnail"]'))
    )
finally:
    browser.find_element(By.XPATH, '//*[@id="items"]/ytd-compact-autoplay-renderer//a[@id="thumbnail"]').click()

try:
    element = WebDriverWait(browser, 100).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="logo-icon-container"]'))
    )
finally:
    browser.find_element(By.XPATH, '//*[@id="logo-icon-container"]').click()

assert "YouTube" in browser.title
assert "youtube" in browser.current_url

#closing
browser.close()
browser.quit()
browser.stop_client()