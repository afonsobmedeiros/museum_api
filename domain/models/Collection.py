from peewee import CharField, ForeignKeyField

from .Exhibition import Exhibition
from infrastructure.database.BaseModel import BaseModel


class Collection(BaseModel):
    name = CharField(max_length=100)
    summary = CharField(max_length=500)
    exhibition = ForeignKeyField(Exhibition)