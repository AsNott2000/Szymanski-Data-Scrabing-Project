from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
import time
from lxml import etree

url = 'https://www.sofascore.com/player/compare?leftPlayerId=847983&leftPlayerSeasonId=63814&leftPlayerTournamentId=52'

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
time.sleep(2)

html = driver.page_source

soup = BeautifulSoup(html, "lxml")

tree = etree.HTML(str(soup))
name = tree.xpath("//div[@class='Box laCmrf']//div[@class='Box Flex ggRYVx iBFqQc']//a//span[@class='Text dypXRD']")[0]
print(name.text)

print("____________________")

age_text_box = soup.find_all("div", class_="Box Flex PAHTS hhKRyf")[0]
age_text = age_text_box.find_all("span")[0]
age = age_text_box.find_all("span")[1]

print(age_text.text)
print(age.text)

print("____________________")

height_text_box = soup.find_all("div", class_="Box Flex PAHTS hhKRyf")[1]
height_text = height_text_box.find_all("span")[0]
height = height_text_box.find_all("span")[1]

print(height_text.text)
print(height.text)

print("____________________")

market_value_box = soup.find_all("div", class_="Box Flex PAHTS hhKRyf")[2]
market_value_text = market_value_box.find_all("span")[0]
market_value = market_value_box.find_all("span")[1]

print(market_value_text.text)
print(market_value.text)

print("____________________")

team_box = soup.find_all("div", class_="Box Flex favGhB hhKRyf")[0]
team_text = team_box.find_all("span")[0]
team = team_box.find_all("span")[1]

print(team_text.text)
print(team.text)

print("____________________")

sofa_rating_box = soup.find("div", class_ ="Box Flex kGzwJG bnpRyo")
sofa_rating_text = sofa_rating_box.find("span", class_="Text gHLcGU")

sofa_rate_box = sofa_rating_box.find_all("div", class_="Box Flex hVZxjR cQgcrM")[0]
sofa_rate = sofa_rate_box.find("span")

print(sofa_rating_text.text)
print(sofa_rate.text)


#excele kaydedilecek
