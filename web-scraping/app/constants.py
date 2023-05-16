import os
from RPA.Robocorp.Vault import Vault

_secret = Vault().get_secret("secretUrl")


DATABASE = "./RTDatabase.db"
BASE_DIR = os.path.dirname(os.path.abspath(__name__))
MOVIE_PATH = os.path.join(BASE_DIR, "files/movies.xlsx")
RESULT_PATH = os.path.join(BASE_DIR, "files/results.xlsx")
URL = _secret["URL"]
MOVIE_BUTTON = "//li[@data-filter='movie']"
MOVIE_SEARCH_RESULTS = "//search-page-result[@type='movie']//a[@class='unset']"
MOVIE_DES_PAGE = "//div[@id='main']"
MOVIE_DETAILS = "//score-board[@data-qa='score-panel']"
STORY_LINE = "//p[@data-qa='movie-info-synopsis']"
REVIEWS = "//review-speech-balloon[@data-qa='critic-review']"
