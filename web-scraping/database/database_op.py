from database.connect_database import DatabaseOperation

def perform_op(data, database) -> None:
    """perform databse operation CREATE UPDATE INSERT and DELETE ONLY

    Args:
        data (dataframe): data frame to inserted
    """
    connection = DatabaseOperation(database)
    connection.insert_excel_to_database(data)
    connection.close_connection()
