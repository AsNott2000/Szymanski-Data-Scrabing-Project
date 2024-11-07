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

defending_soup = soup.find_all("div", class_="Box dFSJzk")[5]
defending_box = defending_soup.find("div", class_="Box Flex ggRYVx cRYpNI")

interceptions_text = defending_box.find_all("span", class_="Text eYrCMI")[0]
interceptions = defending_box.find_all("span", class_="Text bcSQzO")[0]


tackles_text = defending_box.find_all("span", class_="Text eYrCMI")[1]
tackles = defending_box.find_all("span", class_="Text bcSQzO")[2]


dribbled_past_text = defending_box.find_all("span", class_="Text eYrCMI")[2]
dribbled_past = defending_box.find_all("span", class_="Text bcSQzO")[4]


clearances_text = defending_box.find_all("span", class_="Text eYrCMI")[3]
clearances = defending_box.find_all("span", class_="Text bcSQzO")[6]


blocked_shots_text = defending_box.find_all("span", class_="Text eYrCMI")[4]
blocked_shots = defending_box.find_all("span", class_="Text bcSQzO")[6]

texts = [ interceptions_text.text, tackles_text.text,dribbled_past_text.text, clearances_text.text, blocked_shots_text.text]
indexes = [interceptions.text, tackles.text, dribbled_past.text,clearances.text, blocked_shots.text]

df = pd.DataFrame([indexes], columns=texts)
df.to_csv('C:/Users/nurul/OneDrive/Masaüstü/Main DEV/Backend/Python/Szymanski Data Scrabing Project/Excel_Files/Szymanski_datas/defending.csv', index=False)
