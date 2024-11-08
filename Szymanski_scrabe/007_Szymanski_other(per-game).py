import pandas as pd
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

outhers_soup = soup.find_all("div", class_="Box dFSJzk")[6]
others_box = outhers_soup.find("div", class_="Box Flex ggRYVx cRYpNI")

succ_dribbles_text = others_box.find_all("span", class_="Text eYrCMI")[0]
succ_dribbles = others_box.find_all("span", class_="Text bcSQzO")[0]


ground_duels_won_text = others_box.find_all("span", class_="Text eYrCMI")[1]
ground_duels_won = others_box.find_all("span", class_="Text bcSQzO")[2]


aerial_duels_won_text = others_box.find_all("span", class_="Text eYrCMI")[2]
aerial_duels_won = others_box.find_all("span", class_="Text bcSQzO")[4]


posession_lost_text = others_box.find_all("span", class_="Text eYrCMI")[3]
posession_lost = others_box.find_all("span", class_="Text bcSQzO")[6]


fouls_text = others_box.find_all("span", class_="Text eYrCMI")[4]
fouls = others_box.find_all("span", class_="Text bcSQzO")[8]


was_fouls_text = others_box.find_all("span", class_="Text eYrCMI")[5]
was_fouls = others_box.find_all("span", class_="Text bcSQzO")[10]

texts = [succ_dribbles_text.text, ground_duels_won_text.text,aerial_duels_won_text.text, posession_lost_text.text,fouls_text.text, was_fouls_text.text]
indexes = [succ_dribbles.text, ground_duels_won.text, aerial_duels_won.text,posession_lost.text, fouls.text, was_fouls.text]

df = pd.DataFrame([indexes], columns=texts)
df.to_csv('C:/Users/nurul/OneDrive/Masaüstü/Main DEV/Backend/Python/Szymanski Data Scrabing Project/Excel_Files/Szymanski_datas/others.csv', index=False)
