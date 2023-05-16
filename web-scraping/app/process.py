import pandas as pd

from app.connect_database import DatabaseOperation
from app.ExcelReader import ExcelReader
from app.browser import Browser
from app.scrape import Scrape
import app.constants as constants


class Process:
    def __init__(self, browser_lib) -> None:
        self.browser_lib = browser_lib
        self.file_path = constants.MOVIE_PATH
        self.serach_values = None
        self.browser = Browser(self.browser_lib)
        self.database  = DatabaseOperation()
        self.scrape = Scrape(self.browser_lib)
        self.extracted_data = pd.DataFrame(
            columns=[
                "movie_name",
                "tomatometer_score",
                "tomatometer_state",
                "audience_score",
                "storyline",
                "rating",
                "genres",
                "review_1",
                "review_2",
                "review_3",
                "review_4",
                "review_5",
                "status",
            ]
        )
    
    def before_run_process(self):
        excel = ExcelReader(self.file_path)
        self.serach_values = excel.read_excel()
    
    def run_process(self):
        for search_value in self.serach_values:
            self.browser.navigate(search_value)
            try:
                match = self.scrape.search_match(search_value)
            except Exception as ex:
                print(ex)
                match = False
            if match:
                movie_info = self.scrape.movie_info(search_value)
                self.extracted_data.loc[len(self.extracted_data)] = movie_info
            else:
                movie_info = {"movie_name": search_value, "status": "No Exact Match Found"}
                self.extracted_data.loc[len(self.extracted_data)] = movie_info
        self.extracted_data.to_excel(constants.RESULT_PATH + "result.xlsx")   
        self.database.insert_to_database(self.extracted_data)
    
    def after_run_process(self):
        self.database.close_connection()
        self.browser.close_browser()

    