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

attacking_soup = soup.find_all("div", class_="Box dFSJzk")[3]
attacking_box = attacking_soup.find("div", class_="Box Flex ggRYVx cRYpNI")

goals_text = attacking_box.find_all("span", class_="Text eYrCMI")[0]
goals = attacking_box.find_all("span", class_="Text bcSQzO")[0]


xg_text = attacking_box.find_all("span", class_="Text eYrCMI")[1]
xg = attacking_box.find_all("span", class_="Text bcSQzO")[2]


goals_per_game_text = attacking_box.find_all("span", class_="Text eYrCMI")[2]
goals_per_game = attacking_box.find_all("span", class_="Text bcSQzO")[4]

shoots_target_box = attacking_box.find("div", class_="Box eWDuuK")

shoots_off_target_box = shoots_target_box.find("div", class_="Box Flex eSXzoW MHPeY")
shoots_off_target_text = shoots_off_target_box.find_all("span")[1]
shoots_off_target = shoots_off_target_box.find_all("span")[0]


shoots_on_target_box = shoots_target_box.find("div", class_="Box Flex bgBPpJ pwoqI")
shoots_on_target_text = shoots_on_target_box.find_all("span")[0]
shoots_on_target = shoots_on_target_box.find_all("span")[1]


Big_chance_missed_text = attacking_box.find_all("span", class_="Text eYrCMI")[3]
Big_chance_missed = attacking_box.find_all("span", class_="Text bcSQzO")[6]


texts = [ goals_text.text, xg_text.text,goals_per_game_text.text, shoots_off_target_text.text, shoots_on_target_text.text,Big_chance_missed_text.text]
indexes = [goals.text, xg.text, goals_per_game.text,shoots_off_target.text, shoots_on_target.text, Big_chance_missed.text]

df = pd.DataFrame([indexes], columns=texts)
df.to_csv('C:/Users/nurul/OneDrive/Masaüstü/Main DEV/Backend/Python/Szymanski Data Scrabing Project/Excel_Files/Mertens_datas/attacking.csv', index=False)
