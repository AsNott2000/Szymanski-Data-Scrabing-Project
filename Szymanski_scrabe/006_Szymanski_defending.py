from Classes.defending import SofaScoreScraper

url = 'https://www.sofascore.com/player/compare?leftPlayerId=847983&leftPlayerSeasonId=63814&leftPlayerTournamentId=52'

scraper = SofaScoreScraper(url)
scraper.load_page()
defending_df = scraper.get_defending_data()
scraper.save_to_csv(defending_df, 'C:/Users/nurul/OneDrive/Masaüstü/Main DEV/Backend/Python/Szymanski Data Scrabing Project/Excel_Files/Szymanski_datas/defending.csv')
scraper.close_driver()


