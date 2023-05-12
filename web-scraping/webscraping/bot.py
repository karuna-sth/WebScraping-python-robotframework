import pandas as pd
import time

from RPA.Browser.Selenium import Selenium

from database.connect_database import DatabaseOperation


class Bot:
    def __init__(self, value) -> None:
        self.value = value
        self.browser_lib = Selenium(auto_close=False)
        self.url = "https://www.rottentomatoes.com/"
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
                "status"
            ]
        )

    def open(self):
        self.browser_lib.open_browser(self.url, "chrome")

    def search_for_movies(self):
        self.browser_lib.input_text(
            '//*[@id="header-main"]/search-algolia/search-algolia-controls/input',
            self.value,
        )
        time.sleep(1)
        self.browser_lib.click_element(
            '//*[@id="header-main"]/search-algolia/search-algolia-controls/a'
        )

    def search_navigate(self):
        self.browser_lib.wait_until_element_is_visible(
            '//*[@id="search-results"]'
        )
        self.browser_lib.click_element("//li[@data-filter='movie']")
        elements = self.browser_lib.get_webelements(
            "//search-page-result[@type='movie']//ul[@slot='list']//a[@class='unset']"
        )
        print(elements)
        for element in elements:
            title = self.browser_lib.get_text(element)
            if title.lower() == self.value.lower():
                link_to_match = self.browser_lib.get_element_attribute(element, "href")
                self.browser_lib.go_to(link_to_match)
                break
        self.browser_lib.wait_until_element_is_visible("//div[@id='main']")

    def movie_info(self):
        tomatometer_score = self.browser_lib.get_element_attribute(
            '//score-board[@data-qa="score-panel"]', "tomatometerscore"
        )
        print(tomatometer_score)
        audience_score = self.browser_lib.get_element_attribute(
            '//score-board[@data-qa="score-panel"]', "audiencescore"
        )
        print(audience_score)
        rating = self.browser_lib.get_element_attribute(
            '//score-board[@data-qa="score-panel"]', "rating"
        )
        tomatometer_state = self.browser_lib.get_element_attribute(
            'xpath=//score-board[@data-qa="score-panel"]', "tomatometerstate"
        )
        self.browser_lib.wait_until_element_is_visible("id:movie-info")
        story_line = self.browser_lib.get_text("//p[@data-qa='movie-info-synopsis']")
        genres = self.browser_lib.get_text('//*[@id="info"]/li[1]/p/span')
        reviews = self.browser_lib.get_webelements(
            '//review-speech-balloon[@data-qa="critic-review"]'
        )
        print(tomatometer_state, story_line, genres)
        review_list = []
        for review in reviews:
            review_list.append(
                self.browser_lib.get_element_attribute(review, "reviewquote")
            )
            if len(review_list) == 5:
                break
        if len(review_list) != 5:
            for _ in range(len(review_list), 5):
                review_list.append(None)
        print(review_list)
        info_list = [
            self.value,
            tomatometer_score,
            tomatometer_state,
            audience_score,
            story_line,
            rating,
            genres,
            review_list[0],
            review_list[1],
            review_list[2],
            review_list[3],
            review_list[4],
            "Success"
        ]
        self.extracted_data.loc[len(self.extracted_data)] = info_list
        self.extracted_data.to_excel("files/result.xlsx")
        print(self.extracted_data)

    def store_data_in_db(self):
        connection = DatabaseOperation(self.extracted_data)
        connection.perform_op()

    def get_data(self):
        self.open()
        self.search_for_movies()
        self.search_navigate()
        self.movie_info()
        self.store_data_in_db()
        # return self.extracted_data
