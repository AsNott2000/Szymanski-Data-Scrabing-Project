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

passes_soup = soup.find_all("div", class_="Box dFSJzk")[4]
passes_box = passes_soup.find("div", class_="Box Flex ggRYVx cRYpNI")

assists_text = passes_box.find_all("span", class_="Text eYrCMI")[0]
assists = passes_box.find_all("span", class_="Text bcSQzO")[0]
print(assists_text.text)
print(assists.text)

print("_____________")

assists_per_game_text = passes_box.find_all("span", class_="Text eYrCMI")[1]
assists_per_game = passes_box.find_all("span", class_="Text bcSQzO")[2]
print(assists_per_game_text.text)
print(assists_per_game.text)

print("_____________")

xa_text = passes_box.find_all("span", class_="Text eYrCMI")[2]
xa = passes_box.find_all("span", class_="Text bcSQzO")[4]
print(xa_text.text)
print(xa.text)

print("_____________")

Big_chances_created_text = passes_box.find_all("span", class_="Text eYrCMI")[3]
Big_chances_created = passes_box.find_all("span", class_="Text bcSQzO")[6]
print(Big_chances_created_text.text)
print(Big_chances_created.text)

print("_____________")

long_balls_text = passes_box.find_all("span", class_="Text eYrCMI")[4]
long_balls = passes_box.find_all("span", class_="Text bcSQzO")[6]
print(long_balls_text.text)
print(long_balls.text)

print("_____________")

crosses_text = passes_box.find_all("span", class_="Text eYrCMI")[5]
crosses = passes_box.find_all("span", class_="Text bcSQzO")[8]
print(crosses_text.text)
print(crosses.text)

print("_____________")