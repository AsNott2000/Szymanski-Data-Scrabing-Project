from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Web sitesine gidin
url = 'https://www.sofascore.com/player/compare?leftPlayerId=847983&leftPlayerSeasonId=63814&leftPlayerTournamentId=52'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
time.sleep(2)

# Canvas öğesine erişin
map = driver.find_elements(By.XPATH, "//div[@class='Box Flex jjTjiX kmJNGq']")[0]

# Bir süre bekleyin, böylece çizim tamamlanabilir
time.sleep(2)

# Canvas öğesinin ekran görüntüsünü alın
map.screenshot("./Heatmaps/Szymanski_heatmap.png")


