import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import time

url = 'https://www.sofascore.com/player/compare?leftPlayerId=32493&leftPlayerSeasonId=63814&leftPlayerTournamentId=52'

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
time.sleep(2)

html = driver.page_source

soup = BeautifulSoup(html, "html.parser")

cards_soup = soup.find_all("div", class_="Box dFSJzk")[7]
cards_box = cards_soup.find("div", class_="Box Flex ggRYVx cRYpNI")

yellow_text = cards_box.find_all("span", class_="Text eYrCMI")[0]
yellow = cards_box.find_all("span", class_="Text bcSQzO")[0]


yellow_red_text = cards_box.find_all("span", class_="Text eYrCMI")[1]
yellow_red = cards_box.find_all("span", class_="Text bcSQzO")[2]


red_text = cards_box.find_all("span", class_="Text eYrCMI")[2]
red = cards_box.find_all("span", class_="Text bcSQzO")[4]


texts = [ yellow_text.text, yellow_red_text.text,red_text.text]
indexes = [yellow.text, yellow_red.text, red.text]

df = pd.DataFrame([indexes], columns=texts)
df.to_csv('C:/Users/nurul/OneDrive/Masaüstü/Main DEV/Backend/Python/Szymanski Data Scrabing Project/Excel_Files/Mertens_datas/discipline.csv', index=False)
