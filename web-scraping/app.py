"""
Main File
"""
import logging
import os
import pandas as pd
from RPA.Browser.Selenium import Selenium

from webscraping.bot import Bot

DATABASE = "./RTDatabase.db"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILEPATH = os.path.join(BASE_DIR, "files/")


def main():
    """main function where execution starts"""
    file_path = FILEPATH + "movies.xlsx"
    data = pd.read_excel(file_path)
    # extracted_data = pd.DataFrame()
    value = data["Movie"][0]
    logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')
    bot = Bot(value)
    bot.get_data()
    
    

if __name__ == "__main__":
    main()
