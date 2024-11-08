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
        cards_soup = self.soup.find_all("div", class_="Box dFSJzk")[box_index]
        cards_box = cards_soup.find("div", class_="Box Flex ggRYVx cRYpNI")
        label = cards_box.find_all("span", class_="Text eYrCMI")[text_index].text
        value = cards_box.find_all("span", class_="Text bcSQzO")[value_index].text
        return label, value

    def get_discipline_data(self):
        yellow_text, yellow = self.extract_match_data(7, 0, 0)
        yellow_red_text, yellow_red = self.extract_match_data(7, 1, 2)
        red_text, red = self.extract_match_data(7, 2, 4)

        texts = [yellow_text, yellow_red_text, red_text]
        indexes = [yellow, yellow_red, red]
        return pd.DataFrame([indexes], columns=texts)

    def save_to_csv(self, df, file_path):
        df.to_csv(file_path, index=False)

    def close_driver(self):
        self.driver.quit()
