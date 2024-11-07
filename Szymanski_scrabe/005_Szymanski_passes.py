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

passes_soup = soup.find_all("div", class_="Box dFSJzk")[4]
passes_box = passes_soup.find("div", class_="Box Flex ggRYVx cRYpNI")

assists_text = passes_box.find_all("span", class_="Text eYrCMI")[0]
assists = passes_box.find_all("span", class_="Text bcSQzO")[0]


assists_per_game_text = passes_box.find_all("span", class_="Text eYrCMI")[1]
assists_per_game = passes_box.find_all("span", class_="Text bcSQzO")[2]


xa_text = passes_box.find_all("span", class_="Text eYrCMI")[2]
xa = passes_box.find_all("span", class_="Text bcSQzO")[4]


Big_chances_created_text = passes_box.find_all("span", class_="Text eYrCMI")[3]
Big_chances_created = passes_box.find_all("span", class_="Text bcSQzO")[6]


long_balls_text = passes_box.find_all("span", class_="Text eYrCMI")[4]
long_balls = passes_box.find_all("span", class_="Text bcSQzO")[8]


crosses_text = passes_box.find_all("span", class_="Text eYrCMI")[5]
crosses = passes_box.find_all("span", class_="Text bcSQzO")[10]


texts = [ assists_text.text, assists_per_game_text.text,xa_text.text, Big_chances_created_text.text, long_balls_text.text, crosses_text.text]
indexes = [assists.text, assists_per_game.text, xa.text,Big_chances_created.text, long_balls.text, crosses.text]

df = pd.DataFrame([indexes], columns=texts)
df.to_csv('C:/Users/nurul/OneDrive/Masaüstü/Main DEV/Backend/Python/Szymanski Data Scrabing Project/Excel_Files/Szymanski_datas/passes.csv', index=False)
