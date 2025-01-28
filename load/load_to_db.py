
from database.database import insert_data


def load_to_db(data):
    insert_data(data)
    print("Data loaded to database successfully!")