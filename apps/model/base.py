from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Base(db.Model):
    __abstract__ =True
    id = db.Column(db.Integer,primary_key=True)

    def setattr(self,f):
        for k,v in f.items():
            if hasattr(self,k) and k != 'id':
                setattr(self,k,v)
from .users import Users