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

def extract_match_data(soup, text_index, value_index):
    defending_soup = soup.find_all("div", class_="Box dFSJzk")[5]
    defending_box = defending_soup.find("div", class_="Box Flex ggRYVx cRYpNI")
    label = defending_box.find_all("span", class_="Text eYrCMI")[text_index].text
    value = defending_box.find_all("span", class_="Text bcSQzO")[value_index].text
    return label, value

interceptions_text, interceptions = extract_match_data(soup, 0,0)
tackles_text, tackles = extract_match_data(soup, 1,2)
dribbled_past_text, dribbled_past = extract_match_data(soup, 2,4)
clearances_text, clearances = extract_match_data(soup, 3,6)
blocked_shots_text, blocked_shots = extract_match_data(soup, 4,8)

texts = [ interceptions_text, tackles_text,dribbled_past_text, clearances_text, blocked_shots_text]
indexes = [interceptions, tackles, dribbled_past,clearances, blocked_shots]

df = pd.DataFrame([indexes], columns=texts)
df.to_csv('C:/Users/nurul/OneDrive/Masaüstü/Main DEV/Backend/Python/Szymanski Data Scrabing Project/Excel_Files/Mertens_datas/defending.csv', index=False)
