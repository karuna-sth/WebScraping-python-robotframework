"""
Main File
"""
import os
import pandas as pd

from database import database_op

DATABASE = "./RTDatabase.db"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILEPATH = os.path.join(BASE_DIR, "files/")


def main():
    """main function where execution starts"""
    file_path = FILEPATH + "result.xlsx"
    data = pd.read_excel(file_path)
    database_op.perform_op(data, DATABASE)

if __name__ == "__main__":
    main()
