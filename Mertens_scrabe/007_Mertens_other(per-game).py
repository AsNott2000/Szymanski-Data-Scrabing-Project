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
    other_soup = soup.find_all("div", class_="Box dFSJzk")[6]
    other_box = other_soup.find("div", class_="Box Flex ggRYVx cRYpNI")
    label = other_box.find_all("span", class_="Text eYrCMI")[text_index].text
    value = other_box.find_all("span", class_="Text bcSQzO")[value_index].text
    return label, value

succ_dribbles_text, succ_dribbles = extract_match_data(soup, 0,0)
ground_duels_won_text, ground_duels_won = extract_match_data(soup, 1,2)
aerial_duels_won_text, aerial_duels_won = extract_match_data(soup, 2,4)
posession_lost_text, posession_lost = extract_match_data(soup, 3,6)
fouls_text, fouls = extract_match_data(soup, 4,8)
was_fouls_text, was_fouls = extract_match_data(soup, 5,10)

texts = [ succ_dribbles_text, ground_duels_won_text,aerial_duels_won_text, posession_lost_text,fouls_text, was_fouls_text]
indexes = [succ_dribbles, ground_duels_won, aerial_duels_won,posession_lost, fouls, was_fouls]

df = pd.DataFrame([indexes], columns=texts)
df.to_csv('C:/Users/nurul/OneDrive/Masaüstü/Main DEV/Backend/Python/Szymanski Data Scrabing Project/Excel_Files/Mertens_datas/others.csv', index=False)
