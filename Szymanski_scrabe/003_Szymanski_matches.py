from Classes.matches import SofaScoreScraper

# Farklı bir URL belirleyin
url = 'https://www.sofascore.com/player/compare?leftPlayerId=847983&leftPlayerSeasonId=63814&leftPlayerTournamentId=52'

# Sınıfı başlat ve işlemleri yap
scraper = SofaScoreScraper(url)
scraper.load_page()
matches_df = scraper.get_match_data()
scraper.save_to_csv(matches_df,'C:/Users/nurul/OneDrive/Masaüstü/Main DEV/Backend/Python/Szymanski Data Scrabing Project/Excel_Files/Szymanski_datas/matches.csv')
scraper.close_driver()



