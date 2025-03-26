import datetime
from peewee import DateTimeField, Database, SqliteDatabase
from playhouse.signals import Model, pre_save

from Parameters import DEBUG


def create_sqlite_instance() -> Database:
    """Update to recieve connection string from config file.

    Returns:
        Database: Database instance.
    """
    return SqliteDatabase("museum.db")
    
    
def create_mysql_instace() -> Database:
    """Update to recieve connection string from config file.

    Returns:
        Database: Database instance.
    """
    return None


def create_database_instance() -> Database:
    if DEBUG:
        return create_sqlite_instance()
    return create_mysql_instace()


class BaseModel(Model):
    created_at = DateTimeField()
    updated_at = DateTimeField()
    
    class Meta:
        database = create_database_instance()
        

@pre_save(sender=BaseModel)
def add_timestamps(model_class, instance, created):
    if (created):
        instance.created_at = datetime.datetime.now(datetime.timezone.utc).astimezone()
    instance.updated_at = datetime.datetime.now(datetime.timezone.utc).astimezone()