from hashlib import md5
from peewee import CharField, IntegerField
from passlib.hash import pbkdf2_sha512 as hsh
from playhouse.signals import pre_save

from Parameters import SECRET
from infrastructure.database.BaseModel import BaseModel


class User(BaseModel):
    name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    email = CharField(max_length=100)
    password = CharField(max_length=256)
    type = IntegerField()
    
    def gen_hash(self):
        _secret = md5(SECRET.encode()).hexdigest()
        _password = md5(self.password.encode()).hexdigest()
        self.password = hsh.hash(_secret+_password)
        
    def verify(self, password):
        _secret = md5(SECRET.encode()).hexdigest()
        _password = md5(password.encode()).hexdigest()
        return hsh.verify(_secret+_password, self.password)
        
        
@pre_save(sender=User)
def prepare_user(_, instance: User, created):
    if (created):
        instance.gen_hash()
    