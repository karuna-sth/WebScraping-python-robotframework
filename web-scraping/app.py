"""
Main File
"""
import logging
import pandas as pd

import constants
from webscraping.bot import Bot




def main():
    """main function where execution starts"""
    # file_path = constants.FILEPATH + "movies.xlsx"
    # data = pd.read_excel(file_path)
    # # extracted_data = pd.DataFrame()
    # value = data["Movie"][0]
    logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')
    bot = Bot()
    bot.get_data()
    
    

if __name__ == "__main__":
    main()
