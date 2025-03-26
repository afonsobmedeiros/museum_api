from . import User
from peewee import CharField, ForeignKeyField, DateTimeField

from infrastructure.database.BaseModel import BaseModel

class Exhibition(BaseModel):
    Name = CharField(max_length=100)
    summary = CharField(max_length=500)
    start_at = DateTimeField()
    finish_at = DateTimeField()
    owner = ForeignKeyField(User)