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
    cards_soup = soup.find_all("div", class_="Box dFSJzk")[7]
    cards_box = cards_soup.find("div", class_="Box Flex ggRYVx cRYpNI")
    label = cards_box.find_all("span", class_="Text eYrCMI")[text_index].text
    value = cards_box.find_all("span", class_="Text bcSQzO")[value_index].text
    return label, value


yellow_text, yellow = extract_match_data(soup, 0, 0)
yellow_red_text, yellow_red = extract_match_data(soup, 1, 2)
red_text, red = extract_match_data(soup, 2, 4)

texts = [yellow_text, yellow_red_text, red_text]
indexes = [yellow, yellow_red, red]

df = pd.DataFrame([indexes], columns=texts)
df.to_csv(
    'C:/Users/nurul/OneDrive/Masaüstü/Main DEV/Backend/Python/Szymanski Data Scrabing '
    'Project/Excel_Files/Szymanski_datas/discipline.csv',
    index=False)
