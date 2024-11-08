from Classes.defending import SofaScoreScraper

url = 'https://www.sofascore.com/player/compare?leftPlayerId=32493&leftPlayerSeasonId=63814&leftPlayerTournamentId=52'

scraper = SofaScoreScraper(url)
scraper.load_page()
defending_df = scraper.get_defending_data()
scraper.save_to_csv(defending_df, 'C:/Users/nurul/OneDrive/Masaüstü/Main DEV/Backend/Python/Szymanski Data Scrabing Project/Excel_Files/Mertens_datas/defending.csv')
scraper.close_driver()