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

outhers_soup = soup.find_all("div", class_="Box dFSJzk")[6]
others_box = outhers_soup.find("div", class_="Box Flex ggRYVx cRYpNI")

succ_dribbles_text = others_box.find_all("span", class_="Text eYrCMI")[0]
succ_dribbles = others_box.find_all("span", class_="Text bcSQzO")[0]
print(succ_dribbles_text.text)
print(succ_dribbles.text)

print("_____________")

ground_duels_won_text = others_box.find_all("span", class_="Text eYrCMI")[1]
ground_duels_won = others_box.find_all("span", class_="Text bcSQzO")[2]
print(ground_duels_won_text.text)
print(ground_duels_won.text)

print("_____________")

aerial_duels_won_text = others_box.find_all("span", class_="Text eYrCMI")[2]
aerial_duels_won = others_box.find_all("span", class_="Text bcSQzO")[4]
print(aerial_duels_won_text.text)
print(aerial_duels_won.text)

print("_____________")

posession_lost_text = others_box.find_all("span", class_="Text eYrCMI")[3]
posession_lost = others_box.find_all("span", class_="Text bcSQzO")[6]
print(posession_lost_text.text)
print(posession_lost.text)

print("_____________")

fouls_text = others_box.find_all("span", class_="Text eYrCMI")[4]
fouls = others_box.find_all("span", class_="Text bcSQzO")[6]
print(fouls_text.text)
print(fouls.text)

print("_____________")

was_fouls_text = others_box.find_all("span", class_="Text eYrCMI")[5]
was_fouls = others_box.find_all("span", class_="Text bcSQzO")[8]
print(was_fouls_text.text)
print(was_fouls.text)


print("_____________")