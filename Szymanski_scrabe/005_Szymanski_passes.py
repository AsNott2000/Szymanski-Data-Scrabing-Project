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

def extract_match_data(soup, text_index, value_index):
    passes_soup = soup.find_all("div", class_="Box dFSJzk")[4]
    passes_box = passes_soup.find("div", class_="Box Flex ggRYVx cRYpNI")
    label = passes_box.find_all("span", class_="Text eYrCMI")[text_index].text
    value = passes_box.find_all("span", class_="Text bcSQzO")[value_index].text
    return label, value

assists_text, assists = extract_match_data(soup, 0,0)
assists_per_game_text, assists_per_game = extract_match_data(soup, 1,2)
xa_text, xa = extract_match_data(soup, 2,4)
Big_chances_created_text, Big_chances_created = extract_match_data(soup, 3,6)
long_balls_text, long_balls = extract_match_data(soup, 4,8)
crosses_text, crosses = extract_match_data(soup, 5,10)


texts = [assists_text, assists_per_game_text,xa_text, Big_chances_created_text, long_balls_text, crosses_text]
indexes = [assists, assists_per_game, xa,Big_chances_created, long_balls, crosses]

df = pd.DataFrame([indexes], columns=texts)
df.to_csv('C:/Users/nurul/OneDrive/Masaüstü/Main DEV/Backend/Python/Szymanski Data Scrabing Project/Excel_Files/Szymanski_datas/passes.csv', index=False)
