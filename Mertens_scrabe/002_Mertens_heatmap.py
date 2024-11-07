from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Web sitesine gidin
url = 'https://www.sofascore.com/player/compare?leftPlayerId=32493&leftPlayerSeasonId=63814&leftPlayerTournamentId=52'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
actions = ActionChains(driver)
time.sleep(2)

map = driver.find_elements(By.XPATH, "//div[@class='Box Flex jjTjiX kmJNGq']")[0]


# 5 kez aşağı ok tuşuna basma komutlarını zincirleyin
for _ in range(5):
    actions.send_keys(Keys.ARROW_DOWN)

# Komutları çalıştırın
actions.perform()

# Kaydırma tamamlandıktan sonra biraz bekleyin
time.sleep(2)

# Canvas öğesinin ekran görüntüsünü alın
map.screenshot("C:/Users/nurul/OneDrive/Masaüstü/Main DEV/Backend/Python/Szymanski Data Scrabing Project/Heatmaps/Mertens_heatmap.png")


