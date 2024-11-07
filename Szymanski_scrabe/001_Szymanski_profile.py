from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd
from lxml import etree

url = 'https://www.sofascore.com/player/compare?leftPlayerId=847983&leftPlayerSeasonId=63814&leftPlayerTournamentId=52'

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
time.sleep(2)

html = driver.page_source

soup = BeautifulSoup(html, "lxml")

#name data
tree = etree.HTML(str(soup))
name = tree.xpath("//div[@class='Box laCmrf']//div[@class='Box Flex ggRYVx iBFqQc']//a//span[@class='Text dypXRD']")[0]

#age data
age_text_box = soup.find_all("div", class_="Box Flex PAHTS hhKRyf")[0]
age_text = age_text_box.find_all("span")[0]
age = age_text_box.find_all("span")[1]

#height data
height_text_box = soup.find_all("div", class_="Box Flex PAHTS hhKRyf")[1]
height_text = height_text_box.find_all("span")[0]
height = height_text_box.find_all("span")[1]

#cost data
market_value_box = soup.find_all("div", class_="Box Flex PAHTS hhKRyf")[2]
market_value_text = market_value_box.find_all("span")[0]
market_value = market_value_box.find_all("span")[1]

#team data
team_box = soup.find_all("div", class_="Box Flex favGhB hhKRyf")[0]
team_text = team_box.find_all("span")[0]
team = team_box.find_all("span")[1]

#rating data
sofa_rating_box = soup.find("div", class_ ="Box Flex kGzwJG bnpRyo")
sofa_rating_text = sofa_rating_box.find("span", class_="Text gHLcGU")
sofa_rate_box = sofa_rating_box.find_all("div", class_="Box Flex hVZxjR cQgcrM")[0]
sofa_rate = sofa_rate_box.find("span")

texts = ["Name", age_text.text, height_text.text,market_value_text.text, team_text.text, sofa_rating_text.text]
indexes = [name.text, age.text, height.text,market_value.text, team.text, sofa_rate.text]

df = pd.DataFrame([indexes], columns = texts)
df.to_csv('C:/Users/nurul/OneDrive/Masaüstü/Main DEV/Backend/Python/Szymanski Data Scrabing Project/Excel_Files/Szymanski_datas/profile.csv', index=False)
#excele kaydedilecek

