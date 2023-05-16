import app.constants as constants

class Browser:
    def __init__(self, browser_lib) -> None:
        self.URL = constants.URL
        self.browser_lib = browser_lib
        self.browser_lib.open_browser("about:blank", "headlesschrome")
    
    def navigate(self, title) -> None:
        self.browser_lib.go_to(self.URL + title)
        
    def close_browser(self) -> None:
        self.browser_lib.close_browser()