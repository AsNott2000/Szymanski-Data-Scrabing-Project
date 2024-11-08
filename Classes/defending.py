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
        defending_soup = self.soup.find_all("div", class_="Box dFSJzk")[box_index]
        defending_box = defending_soup.find("div", class_="Box Flex ggRYVx cRYpNI")
        label = defending_box.find_all("span", class_="Text eYrCMI")[text_index].text
        value = defending_box.find_all("span", class_="Text bcSQzO")[value_index].text
        return label, value

    def get_defending_data(self):
        interceptions_text, interceptions = self.extract_match_data(5, 0, 0)
        tackles_text, tackles = self.extract_match_data(5, 1, 2)
        dribbled_past_text, dribbled_past = self.extract_match_data(5, 2, 4)
        clearances_text, clearances = self.extract_match_data(5, 3, 6)
        blocked_shots_text, blocked_shots = self.extract_match_data(5, 4, 8)

        texts = [interceptions_text, tackles_text, dribbled_past_text, clearances_text, blocked_shots_text]
        indexes = [interceptions, tackles, dribbled_past, clearances, blocked_shots]
        return pd.DataFrame([indexes], columns=texts)

    def save_to_csv(self, df, file_path):
        df.to_csv(file_path, index=False)

    def close_driver(self):
        self.driver.quit()
