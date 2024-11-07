from selenium import webdriver
from bs4 import BeautifulSoup
import time

url = 'https://www.sofascore.com/player/compare?leftPlayerId=847983&leftPlayerSeasonId=63814&leftPlayerTournamentId=52'

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
print(min_per_game_text.text)
print(min_per_game.text)

print("_____________")

total_min_play_text = matches_box.find_all("span", class_="Text eYrCMI")[1]
total_min_play = matches_box.find_all("span", class_="Text bcSQzO")[2]
print(total_min_play_text.text)
print(total_min_play.text)

print("_____________")

appereances_text = matches_box.find_all("span", class_="Text eYrCMI")[2]
appereances = matches_box.find_all("span", class_="Text bcSQzO")[4]
print(appereances_text.text)
print(appereances.text)