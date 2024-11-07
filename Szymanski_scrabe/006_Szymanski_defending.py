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

defending_soup = soup.find_all("div", class_="Box dFSJzk")[5]
defending_box = defending_soup.find("div", class_="Box Flex ggRYVx cRYpNI")

interceptions_text = defending_box.find_all("span", class_="Text eYrCMI")[0]
interceptions = defending_box.find_all("span", class_="Text bcSQzO")[0]
print(interceptions_text.text)
print(interceptions.text)

print("_____________")

tackles_text = defending_box.find_all("span", class_="Text eYrCMI")[1]
tackles = defending_box.find_all("span", class_="Text bcSQzO")[2]
print(tackles_text.text)
print(tackles.text)

print("_____________")

dribbled_past_text = defending_box.find_all("span", class_="Text eYrCMI")[2]
dribbled_past = defending_box.find_all("span", class_="Text bcSQzO")[4]
print(dribbled_past_text.text)
print(dribbled_past.text)

print("_____________")

clearances_text = defending_box.find_all("span", class_="Text eYrCMI")[3]
clearances = defending_box.find_all("span", class_="Text bcSQzO")[6]
print(clearances_text.text)
print(clearances.text)

print("_____________")

blocked_shots_text = defending_box.find_all("span", class_="Text eYrCMI")[4]
blocked_shots = defending_box.find_all("span", class_="Text bcSQzO")[6]
print(blocked_shots_text.text)
print(blocked_shots.text)

print("_____________")