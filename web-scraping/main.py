"""
Main File
"""

from RPA.Browser.Selenium import Selenium
from app.process import Process

def main():
    """main function where execution starts"""
    browser_lib = Selenium(auto_close=False)
    process = Process(browser_lib)
    process.before_run_process()
    process.run_process()
    process.after_run_process()   

if __name__ == "__main__":
    main()
