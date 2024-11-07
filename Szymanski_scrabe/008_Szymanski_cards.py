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

cards_soup = soup.find_all("div", class_="Box dFSJzk")[7]
cards_box = cards_soup.find("div", class_="Box Flex ggRYVx cRYpNI")

yellow_text = cards_box.find_all("span", class_="Text eYrCMI")[0]
yellow = cards_box.find_all("span", class_="Text bcSQzO")[0]
print(yellow_text.text)
print(yellow.text)

print("_____________")

yellow_red_text = cards_box.find_all("span", class_="Text eYrCMI")[1]
yellow_red = cards_box.find_all("span", class_="Text bcSQzO")[2]
print(yellow_red_text.text)
print(yellow_red.text)

print("_____________")

red_text = cards_box.find_all("span", class_="Text eYrCMI")[2]
red = cards_box.find_all("span", class_="Text bcSQzO")[4]
print(red_text.text)
print(red.text)

print("_____________")