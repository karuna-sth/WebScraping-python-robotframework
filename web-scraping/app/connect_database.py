"""
This module provides funcitonality to connect to database
"""

import sqlite3
import pandas as pd
import app.constants as constants


class DatabaseOperation:
    """Connects to a database"""

    def __init__(self) -> None:
        self.conn = None
        self.cursor = None
        self.database = constants.DATABASE
        try:
            self.conn = sqlite3.connect(self.database)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as ex:
            print(ex)
        self.create_table()

    def close_connection(self) -> None:
        """closes connection"""
        try:
            if self.conn:
                self.conn.close()
        except Exception as ex:
            print(ex)
            

    def create_table(self) -> None:
        """execute sql query for create, update, delete, insert

        Args:
            query (str): query for create, update, delete or insert
        """
        query = """
            CREATE TABLE IF NOT EXISTS Movies( 
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                movie_name TEXT NOT NULL, 
                tomatometer_score TEXT, 
                tomatometer_state TEXT,
                audience_score TEXT, 
                storyline TEXT, 
                rating TEXT, 
                genres TEXT, 
                review_1 TEXT, 
                review_2 TEXT, 
                review_3 TEXT, 
                review_4 TEXT,  
                review_5 TEXT, 
                status TEXT NOT NULL);
            """
        self.cursor.execute(query)
        self.conn.commit()

    def insert_to_database(self, data: pd.DataFrame) -> None:
        """insert data generated from excel to database

        Args:
            file_path (str): path to excel file
        """
        try:
            data.to_sql("Movies", self.conn, if_exists="append", index=False)
        except Exception as ex:
            print(ex)

