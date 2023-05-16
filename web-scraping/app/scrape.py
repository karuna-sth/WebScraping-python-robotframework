import pandas as pd
import time

import app.constants as constants


class Scrape:
    def __init__(self, browser_lib) -> None:
        self.browser_lib = browser_lib

    def search_match(self, title):
        self.browser_lib.wait_until_element_is_visible(constants.MOVIE_BUTTON,timeout=30)
        self.browser_lib.click_element(constants.MOVIE_BUTTON)
        elements = self.browser_lib.get_webelements(
            constants.MOVIE_SEARCH_RESULTS
        )
        print(elements)
        link_to_match = None
        for element in elements:
            title_browser = self.browser_lib.get_text(element)
            if title_browser.strip().lower() == title.strip().lower():
                link_to_match = self.browser_lib.get_element_attribute(element, "href")
                self.browser_lib.go_to(link_to_match)
                break
        if link_to_match is None:
            return False
        self.browser_lib.wait_until_element_is_visible(constants.MOVIE_DES_PAGE, timeout=30)
        return True

    def movie_info(self, title):
        tomatometer_score = self.browser_lib.get_element_attribute(
            constants.MOVIE_DETAILS, "tomatometerscore"
        )
        print(tomatometer_score)
        audience_score = self.browser_lib.get_element_attribute(
            constants.MOVIE_DETAILS, "audiencescore"
        )
        print(audience_score)
        rating = self.browser_lib.get_element_attribute(
            constants.MOVIE_DETAILS, "rating"
        )
        tomatometer_state = self.browser_lib.get_element_attribute(
            constants.MOVIE_DETAILS, "tomatometerstate"
        )
        genres = self.browser_lib.get_element_attribute(constants.MOVIE_DETAILS, "innerText")
        genres = (genres.split(",")[1]).split("\n")[0]
        story_line = self.browser_lib.get_text(constants.STORY_LINE)
        
        print(genres)
        reviews = self.browser_lib.get_webelements(
            constants.REVIEWS
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
                review_list.append("Not Found")
        print(review_list)
        info_list = [
            title,
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
            "Success",
        ]
        print(info_list)
        info_list = ["Not Found" if x is None or x == "" else x for x in info_list]
        print(info_list)
        return (info_list)

    # def get_data(self):
    #     self.open()
    #     # file_path = constants.FILEPATH + "movies.xlsx"
    #     # search_values = pd.read_excel(file_path)
    #     print(search_values)
    #     for search_value in search_values["Movie"]:
    #         print(search_value)
    #         try:
    #             self.title = search_value
    #             self.search_for_movies()
    #             status = self.search_navigate()
    #             if status:
    #                 self.movie_info()
    #             else:
    #                 new_row = {'movie_name': self.title, 'status': "No Exact match Found"}
    #                 self.extracted_data.loc[len(self.extracted_data)] = new_row
    #             self.store_data_in_db()
    #         except Exception as ex:
    #             print(ex)
    #             continue
