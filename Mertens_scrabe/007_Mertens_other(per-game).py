from Classes.others import SofaScoreScraper

# Farklı bir URL belirleyin
url = 'https://www.sofascore.com/player/compare?leftPlayerId=32493&leftPlayerSeasonId=63814&leftPlayerTournamentId=52'

# Sınıfı başlat ve işlemleri yap
scraper = SofaScoreScraper(url)
scraper.load_page()
others_df = scraper.get_others_data()
scraper.save_to_csv(others_df, 'C:/Users/nurul/OneDrive/Masaüstü/Main DEV/Backend/Python/Szymanski Data Scrabing Project/Excel_Files/Mertens_datas/others.csv')
scraper.close_driver()