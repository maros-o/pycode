from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = 'https://www.youtube.com/watch?v=31YPimnHdfM'
driver = webdriver.Chrome(executable_path='./chromedriver.exe')

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(chrome_options=options)

driver.get(url)

driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[4]/form').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="movie_player"]/div[24]/div[2]/div[1]/button').click()

driver.execute_script("window.scrollTo(0, 400)")
time.sleep(0.5)

for x in range(10):
    driver.execute_script("window.scrollTo(0, 100000)")
    print("waiting for load:", x, "seconds")
    time.sleep(0.5)

time.sleep(0.2)
comments = driver.find_element_by_id("comments")
nicknames = comments.find_elements_by_id("author-text")
for nickname in nicknames :
    print(nickname.text)
print("\n number of nicknames: ", len(nicknames))