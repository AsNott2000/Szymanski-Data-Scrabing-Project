# sofascore_scraper.py

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
        time.sleep(2)  # Sayfanın tam yüklenmesi için bekleme
        html = self.driver.page_source
        self.soup = BeautifulSoup(html, "html.parser")

    def extract_match_data(self, box_index, text_index, value_index):
        passes_soup = self.soup.find_all("div", class_="Box dFSJzk")[box_index]
        passes_box = passes_soup.find("div", class_="Box Flex ggRYVx cRYpNI")
        label = passes_box.find_all("span", class_="Text eYrCMI")[text_index].text
        value = passes_box.find_all("span", class_="Text bcSQzO")[value_index].text
        return label, value

    def get_passes_data(self):
        assists_text, assists = self.extract_match_data(4, 0, 0)
        assists_per_game_text, assists_per_game = self.extract_match_data(4, 1, 2)
        xa_text, xa = self.extract_match_data(4, 2, 4)
        Big_chances_created_text, Big_chances_created = self.extract_match_data(4, 3, 6)
        long_balls_text, long_balls = self.extract_match_data(4, 4, 8)
        crosses_text, crosses = self.extract_match_data(4, 5, 10)

        texts = [assists_text, assists_per_game_text, xa_text, Big_chances_created_text, long_balls_text, crosses_text]
        indexes = [assists, assists_per_game, xa, Big_chances_created, long_balls, crosses]
        return pd.DataFrame([indexes], columns=texts)

    def save_to_csv(self, df, file_path):
        df.to_csv(file_path, index=False)

    def close_driver(self):
        self.driver.quit()
