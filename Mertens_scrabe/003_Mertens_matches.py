from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd

url = 'https://www.sofascore.com/player/compare?leftPlayerId=32493&leftPlayerSeasonId=63814&leftPlayerTournamentId=52'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
time.sleep(2)

html = driver.page_source

soup = BeautifulSoup(html, "html.parser")

matches_soup = soup.find_all("div", class_="Box dFSJzk")[2]
matches_box = matches_soup.find("div", class_="Box Flex ggRYVx cRYpNI")


min_per_game_text = matches_box.find_all("span", class_="Text eYrCMI")[0]
min_per_game = matches_box.find_all("span", class_="Text bcSQzO")[0]


total_min_play_text = matches_box.find_all("span", class_="Text eYrCMI")[1]
total_min_play = matches_box.find_all("span", class_="Text bcSQzO")[2]


appereances_text = matches_box.find_all("span", class_="Text eYrCMI")[2]
appereances = matches_box.find_all("span", class_="Text bcSQzO")[4]

texts = [min_per_game_text.text, total_min_play_text.text, appereances_text.text]
indexes = [min_per_game.text, total_min_play.text, appereances.text]

df = pd.DataFrame([indexes], columns = texts)
df.to_csv('C:/Users/nurul/OneDrive/Masaüstü/Main DEV/Backend/Python/Szymanski Data Scrabing Project/Excel_Files/Mertens_datas/matches.csv', index=False)