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
shoots_target_box = attacking_box.find("div", class_="Box eWDuuK")

shoots_off_target_box = shoots_target_box.find("div", class_="Box Flex eSXzoW MHPeY")
shoots_off_target_text = shoots_off_target_box.find_all("span")[1]
shoots_off_target = shoots_off_target_box.find_all("span")[0]

shoots_on_target_box = shoots_target_box.find("div", class_="Box Flex bgBPpJ pwoqI")
shoots_on_target_text = shoots_on_target_box.find_all("span")[0]
shoots_on_target = shoots_on_target_box.find_all("span")[1]

def extract_match_data(soup, text_index, value_index):
    label = attacking_box.find_all("span", class_="Text eYrCMI")[text_index].text
    value = attacking_box.find_all("span", class_="Text bcSQzO")[value_index].text
    return label, value

goals_text, goals = extract_match_data(soup, 0,0)
xg_text, xg = extract_match_data(soup, 1,2)
goals_per_game_text, goals_per_game = extract_match_data(soup, 2,4)
Big_chance_missed_text, Big_chance_missed = extract_match_data(soup, 3,6)



texts = [ goals_text, xg_text, goals_per_game_text, shoots_off_target_text.text, shoots_on_target_text.text,Big_chance_missed_text]
indexes = [goals, xg, goals_per_game,shoots_off_target.text, shoots_on_target.text, Big_chance_missed]

df = pd.DataFrame([indexes], columns=texts)
df.to_csv('C:/Users/nurul/OneDrive/Masaüstü/Main DEV/Backend/Python/Szymanski Data Scrabing Project/Excel_Files/Mertens_datas/attacking.csv', index=False)
