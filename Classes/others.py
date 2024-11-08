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
        other_soup = self.soup.find_all("div", class_="Box dFSJzk")[box_index]
        other_box = other_soup.find("div", class_="Box Flex ggRYVx cRYpNI")
        label = other_box.find_all("span", class_="Text eYrCMI")[text_index].text
        value = other_box.find_all("span", class_="Text bcSQzO")[value_index].text
        return label, value

    def get_others_data(self):
        succ_dribbles_text, succ_dribbles = self.extract_match_data(6, 0, 0)
        ground_duels_won_text, ground_duels_won = self.extract_match_data(6, 1, 2)
        aerial_duels_won_text, aerial_duels_won = self.extract_match_data(6, 2, 4)
        posession_lost_text, posession_lost = self.extract_match_data(6, 3, 6)
        fouls_text, fouls = self.extract_match_data(6, 4, 8)
        was_fouls_text, was_fouls = self.extract_match_data(6, 5, 10)

        texts = [succ_dribbles_text, ground_duels_won_text, aerial_duels_won_text, posession_lost_text, fouls_text,
                 was_fouls_text]
        indexes = [succ_dribbles, ground_duels_won, aerial_duels_won, posession_lost, fouls, was_fouls]
        return pd.DataFrame([indexes], columns=texts)

    def save_to_csv(self, df, file_path):
        df.to_csv(file_path, index=False)

    def close_driver(self):
        self.driver.quit()
