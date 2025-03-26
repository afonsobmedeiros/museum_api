from peewee import CharField, DateField, ForeignKeyField, TextField

from . import User, Collection
from infrastructure.database.BaseModel import BaseModel


class Piece(BaseModel):
    photo = TextField()
    subtitle = CharField(max_length=200)
    summary = CharField(max_length=500)
    date = DateField()
    author = ForeignKeyField(User)
    collection = ForeignKeyField(Collection)
