from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Web sitesine gidin
url = 'https://www.sofascore.com/player/compare?leftPlayerId=847983&leftPlayerSeasonId=63814&leftPlayerTournamentId=52'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
actions = ActionChains(driver)
# 5 kez aşağı ok tuşuna basma komutlarını zincirleyin
for _ in range(5):
    actions.send_keys(Keys.ARROW_DOWN)
# Komutları çalıştırın
actions.perform()
time.sleep(2)

# Canvas öğesine erişin
map = driver.find_elements(By.XPATH, "//div[@class='Box Flex jjTjiX kmJNGq']")[0]


# Bir süre bekleyin, böylece çizim tamamlanabilir
time.sleep(2)

# Canvas öğesinin ekran görüntüsünü alın
map.screenshot("C:/Users/nurul/OneDrive/Masaüstü/Main DEV/Backend/Python/Szymanski Data Scrabing Project/Heatmaps/Mertens_heatmap.png/Szymanski_heatmap.png")


