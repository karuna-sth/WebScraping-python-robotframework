import pandas as pd

class ExcelReader:
    def __init__(self, file_path) -> None:
        self.file_path = file_path
    
    def read_excel(self) -> list:
        try:
            search_values = pd.read_excel(self.file_path)
            search_values = search_values['Movie']
            return search_values
        except Exception as ex:
            print(ex)
        return None
