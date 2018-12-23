from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time


words = ["hello world", "comment 1", "new comment", "this is selenium", "from selenium", "watching tv", "so cold", "the babysitter", "reading books"]
pics = ["pic-6.png", "pic-5.png", "pic-4.png", "pic-3.png", "pic-2.png", "pic-1.png"]
filepath = "C:\\Users\\ryan\\Desktop\\pics\\"

#launching the browser
browser=webdriver.Firefox()
browser.maximize_window()
browser.get('https://automation.dev.coinspectapp.com/')

#logging in
browser.find_element(By.XPATH, '//input[@name="email"]').send_keys('qa_technicaltest')
browser.find_element(By.XPATH, '//input[@name="password"]').send_keys('QWERTYqwerty123!@#')
browser.find_element(By.XPATH, '//input[@value="Login"]').click()

#getting the current value of DONE
prv_DONE = browser.find_element(By.XPATH, '//h6[contains(.,"DONE")]/preceding-sibling::h1').text

#creating a new inspection
try:
    element = WebDriverWait(browser, 100).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="impromptuShortcut"]/div[@ng-click="openImpromptuForm()"]'))
    )
finally:
    browser.find_element(By.XPATH, '//*[@id="impromptuShortcut"]/div[@ng-click="openImpromptuForm()"]').click()

try:
    element = WebDriverWait(browser, 100).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="create-inspection"]'))
    )
finally:
    browser.find_element(By.XPATH, '//*[@id="withOutUnitsDropdown"]').click()

try:
    element = WebDriverWait(browser, 100).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="withOutUnitsDropdown-overlay"]//span[contains(.,"Automation A")]'))
    )
finally:
    browser.find_element(By.XPATH, '//*[@id="withOutUnitsDropdown-overlay"]//span[contains(.,"Automation A")]').click()

try:
    element = WebDriverWait(browser, 100).until(
        EC.presence_of_element_located((By.XPATH, '//label[contains(.,"Checklist")]'))
    )
finally:
    browser.find_element(By.XPATH, '//*[@id="impromptuChecklistDropdown"]').click()

try:
    element = WebDriverWait(browser, 100).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="impromptuChecklistDropdown-overlay"]//span[contains(.,"Automated Color Test")]'))
    )
finally:
    browser.find_element(By.XPATH, '//*[@id="impromptuChecklistDropdown-overlay"]//span[contains(.,"Automated Color Test")]').click()

browser.find_element(By.XPATH, '//button[@ng-click="create()"]').click()

#start answering questions
try:
    element = WebDriverWait(browser, 100).until(
        EC.presence_of_element_located((By.XPATH, '//header[@ng-click="group.expanded = !group.expanded"]'))
    )
finally:
    browser.find_element(By.XPATH, '//header[@ng-click="group.expanded = !group.expanded"]').click()

try:
    element = WebDriverWait(browser, 100).until(
        EC.presence_of_element_located((By.XPATH, '//header[@ng-click="group.expanded = !group.expanded"]/following-sibling::ul/li[1]'))
    )
finally:
    browser.find_element(By.XPATH, '//header[@ng-click="group.expanded = !group.expanded"]/following-sibling::ul/li[1]').click()

#randomizing the answers for Q1
try:
    element = WebDriverWait(browser, 100).until(
        EC.presence_of_element_located((By.XPATH, '//label[contains(.,"Answer")]/following-sibling::div/div'))
    )
finally:
    count_options = browser.find_elements(By.XPATH, '//label[contains(.,"Answer")]/following-sibling::div/div')

rand_ans = random.randint(1,len(count_options))
browser.find_element(By.XPATH, '//label[contains(.,"Answer")]/following-sibling::div/div['+str(rand_ans)+']').click()
rand_comment = random.choice(words)
browser.find_element(By.XPATH, '//textarea').send_keys(rand_comment)
rand_pic = random.choice(pics)

try:
    element = WebDriverWait(browser, 100).until(
        EC.presence_of_element_located((By.XPATH, '//input[@capture="camera" and @type="file"]'))
    )
finally:
    browser.find_element(By.XPATH, '//input[@capture="camera" and @type="file"]').send_keys(filepath+rand_pic)

try:
    element = WebDriverWait(browser, 100).until(
        EC.presence_of_element_located((By.XPATH, '//figure[@ng-click="edit(img)"]'))
    )
finally:
    browser.find_element(By.XPATH, '//figure[@ng-click="edit(img)"]').click()

rand_comment = random.choice(words)

try:
    element = WebDriverWait(browser, 100).until(
        EC.presence_of_element_located((By.XPATH, '//textarea[@ng-model="img.comment"]'))
    )
finally:
    browser.find_element(By.XPATH, '//textarea[@ng-model="img.comment"]').click()

browser.find_element(By.XPATH, '//textarea[@ng-model="img.comment"]').send_keys(rand_comment)
browser.find_element(By.XPATH, '//h3[@ng-click="doNext()"]').click()

#question 2
try:
    element = WebDriverWait(browser, 100).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="ca-dropdown-0"]'))
    )
finally:
    browser.find_element(By.XPATH, '//*[@id="ca-dropdown-0"]').click()

count_options = browser.find_elements(By.XPATH, '//*[@id="ca-dropdown-0-overlay"]/div[2]/div')
rand_ans = random.randint(1,len(count_options))
browser.find_element(By.XPATH, '//*[@id="ca-dropdown-0-overlay"]/div[2]/div['+str(rand_ans)+']').click()
rand_comment = random.choice(words)
browser.find_element(By.XPATH, '//textarea').send_keys(rand_comment)
rand_pic = random.choice(pics)

try:
    element = WebDriverWait(browser, 100).until(
        EC.presence_of_element_located((By.XPATH, '//input[@capture="camera" and @type="file"]'))
    )
finally:
    browser.find_element(By.XPATH, '//input[@capture="camera" and @type="file"]').send_keys(filepath+rand_pic)

try:
    element = WebDriverWait(browser, 100).until(
        EC.presence_of_element_located((By.XPATH, '//figure[@ng-click="edit(img)"]'))
    )
finally:
    browser.find_element(By.XPATH, '//figure[@ng-click="edit(img)"]').click()

rand_comment = random.choice(words)

try:
    element = WebDriverWait(browser, 100).until(
        EC.presence_of_element_located((By.XPATH, '//textarea[@ng-model="img.comment"]'))
    )
finally:
    browser.find_element(By.XPATH, '//textarea[@ng-model="img.comment"]').click()

browser.find_element(By.XPATH, '//textarea[@ng-model="img.comment"]').send_keys(rand_comment)
browser.find_element(By.XPATH, '//h3[@ng-click="doNext()"]').click()

#question 3
try:
    element = WebDriverWait(browser, 100).until(
        EC.presence_of_element_located((By.XPATH, '//label[contains(.,"Answer")]/following-sibling::div/div'))
    )
finally:
    count_options = browser.find_elements(By.XPATH, '//label[contains(.,"Answer")]/following-sibling::div/div')

rand_ans = random.randint(1,len(count_options))
browser.find_element(By.XPATH, '//label[contains(.,"Answer")]/following-sibling::div/div['+str(rand_ans)+']').click()
rand_comment = random.choice(words)
browser.find_element(By.XPATH, '//textarea').send_keys(rand_comment)
rand_pic = random.choice(pics)

try:
    element = WebDriverWait(browser, 100).until(
        EC.presence_of_element_located((By.XPATH, '//input[@capture="camera" and @type="file"]'))
    )
finally:
    browser.find_element(By.XPATH, '//input[@capture="camera" and @type="file"]').send_keys(filepath+rand_pic)

try:
    element = WebDriverWait(browser, 100).until(
        EC.presence_of_element_located((By.XPATH, '//figure[@ng-click="edit(img)"]'))
    )
finally:
    browser.find_element(By.XPATH, '//figure[@ng-click="edit(img)"]').click()

rand_comment = random.choice(words)

try:
    element = WebDriverWait(browser, 100).until(
        EC.presence_of_element_located((By.XPATH, '//textarea[@ng-model="img.comment"]'))
    )
finally:
    browser.find_element(By.XPATH, '//textarea[@ng-model="img.comment"]').click()

browser.find_element(By.XPATH, '//textarea[@ng-model="img.comment"]').send_keys(rand_comment)
browser.find_element(By.XPATH, '//h3[@ng-click="doNext()"]').click()

#question 4
try:
    element = WebDriverWait(browser, 100).until(
        EC.presence_of_element_located((By.XPATH, '//input[@ng-change="ngChange()"]'))
    )
finally:
    rand_ans = random.randint(1,20)
    browser.find_element(By.XPATH, '//input[@ng-change="ngChange()"]').send_keys(rand_ans)

rand_comment = random.choice(words)
browser.find_element(By.XPATH, '//textarea').send_keys(rand_comment)
rand_pic = random.choice(pics)

try:
    element = WebDriverWait(browser, 100).until(
        EC.presence_of_element_located((By.XPATH, '//input[@capture="camera" and @type="file"]'))
    )
finally:
    browser.find_element(By.XPATH, '//input[@capture="camera" and @type="file"]').send_keys(filepath+rand_pic)

try:
    element = WebDriverWait(browser, 100).until(
        EC.presence_of_element_located((By.XPATH, '//figure[@ng-click="edit(img)"]'))
    )
finally:
    browser.find_element(By.XPATH, '//figure[@ng-click="edit(img)"]').click()

rand_comment = random.choice(words)

try:
    element = WebDriverWait(browser, 100).until(
        EC.presence_of_element_located((By.XPATH, '//textarea[@ng-model="img.comment"]'))
    )
finally:
    browser.find_element(By.XPATH, '//textarea[@ng-model="img.comment"]').click()

browser.find_element(By.XPATH, '//textarea[@ng-model="img.comment"]').send_keys(rand_comment)
browser.find_element(By.XPATH, '//h3[@ng-click="doNext()"]').click()

#marking it DONE
try:
    element = WebDriverWait(browser, 100).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="mark-as-done"]'))
    )
finally:
    browser.find_element(By.XPATH, '//*[@id="mark-as-done"]').click()

try:
    element = WebDriverWait(browser, 100).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="confirm-modal"]'))
    )
finally:
    browser.find_element(By.XPATH, '//button[contains(.,"Confirm")]').click()

#creating a report
try:
    element = WebDriverWait(browser, 100).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="create-report"]'))
    )
finally:
    time.sleep(5)
    browser.find_element(By.XPATH, '//*[@id="create-report"]').click()

main_window = browser.current_window_handle

try:
    element = WebDriverWait(browser, 100).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="download"]'))
    )
finally:
    time.sleep(40)
    browser.find_element(By.XPATH, '//*[@id="download"]').click()

#switching back to main tab
browser.switch_to_window(main_window)

try:
    element = WebDriverWait(browser, 100).until(
        EC.presence_of_element_located((By.XPATH, '//div[@class="hamburger-button i-hamburger"]'))
    )
finally:
    browser.find_element(By.XPATH, '//div[@class="hamburger-button i-hamburger"]').click()

try:
    element = WebDriverWait(browser, 100).until(
        EC.presence_of_element_located((By.XPATH, '//a//span[contains(.,"Home")]'))
    )
finally:
    time.sleep(5)
    browser.find_element(By.XPATH, '//a//span[contains(.,"Home")]').click()

#checking if DONE count has increased
time.sleep(10)
inc_DONE = browser.find_element(By.XPATH, '//h6[contains(.,"DONE")]/preceding-sibling::h1').text

if inc_DONE>prv_DONE:
    pass

#logging out
try:
    element = WebDriverWait(browser, 100).until(
        EC.presence_of_element_located((By.XPATH, '//div[@class="hamburger-button i-hamburger"]'))
    )
finally:
    browser.find_element(By.XPATH, '//div[@class="hamburger-button i-hamburger"]').click()

try:
    element = WebDriverWait(browser, 100).until(
        EC.presence_of_element_located((By.XPATH, '//a//span[contains(.,"Logout")]'))
    )
finally:
    time.sleep(5)
    browser.find_element(By.XPATH, '//a//span[contains(.,"Logout")]').click()

#closing
browser.close()
browser.quit()
browser.stop_client()