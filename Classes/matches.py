import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import time


class SofaScoreScraper:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome()
        self.soup = None

    def load_page(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        time.sleep(2)
        html = self.driver.page_source
        self.soup = BeautifulSoup(html, "html.parser")

    def extract_match_data(self, box_index, text_index, value_index):
        matches_soup = self.soup.find_all("div", class_="Box dFSJzk")[box_index]
        matches_box = matches_soup.find("div", class_="Box Flex ggRYVx cRYpNI")
        label = matches_box.find_all("span", class_="Text eYrCMI")[text_index].text
        value = matches_box.find_all("span", class_="Text bcSQzO")[value_index].text
        return label, value

    def get_match_data(self):
        min_per_game_text, min_per_game = self.extract_match_data(2, 0, 0)
        total_min_play_text, total_min_play = self.extract_match_data(2, 1, 2)
        appereances_text, appereances = self.extract_match_data(2, 2, 4)

        texts = [min_per_game_text, total_min_play_text, appereances_text]
        indexes = [min_per_game, total_min_play, appereances]
        return pd.DataFrame([indexes], columns=texts)

    def save_to_csv(self, df, file_path):
        df.to_csv(file_path, index=False)

    def close_driver(self):
        self.driver.quit()
