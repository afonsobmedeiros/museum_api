from peewee import Model
from domain.models import User, Exhibition, Collection, Piece
from infrastructure.database.BaseModel import create_database_instance

tables: list[Model] = [
    User,
    Exhibition,
    Collection,
    Piece
]

def create_tables():
    print("Creating tables:\n")
    for table in tables:
        try:
            print("Creating table: " + str(table))
            table.create_table()
        except Exception as e:
            print(f"Error on creating table: {str(table)} - {e}")
            
if __name__ == "__main__":
    create_tables()