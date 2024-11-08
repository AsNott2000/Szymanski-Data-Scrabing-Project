from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd

url = 'https://www.sofascore.com/player/compare?leftPlayerId=32493&leftPlayerSeasonId=63814&leftPlayerTournamentId=52'

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
time.sleep(2)

html = driver.page_source

soup = BeautifulSoup(html, "html.parser")

"""
    Belirtilen indexlere göre maç istatistiklerini çeker.
    Parameters:
        - soup: BeautifulSoup nesnesi
        - text_index: İstatistik başlığı için kullanılan index
        - value_index: İstatistik değeri için kullanılan index
    Returns:
        - label, value: Başlık ve değeri döndürür
    """
def extract_match_data(soup, text_index, value_index):
    matches_soup = soup.find_all("div", class_="Box dFSJzk")[2]
    matches_box = matches_soup.find("div", class_="Box Flex ggRYVx cRYpNI")
    label = matches_box.find_all("span", class_="Text eYrCMI")[text_index].text
    value = matches_box.find_all("span", class_="Text bcSQzO")[value_index].text
    return label, value


min_per_game_text, min_per_game = extract_match_data(soup, 0,0)
total_min_play_text, total_min_play = extract_match_data(soup, 1, 2)
appereances_text, appereances = extract_match_data(soup, 2,4)

texts = [min_per_game_text, total_min_play_text, appereances_text]
indexes = [min_per_game, total_min_play, appereances]

df = pd.DataFrame([indexes], columns=texts)
df.to_csv('C:/Users/nurul/OneDrive/Masaüstü/Main DEV/Backend/Python/Szymanski Data Scrabing Project/Excel_Files/Mertens_datas/matches.csv', index=False)