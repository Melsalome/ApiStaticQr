# from flask_sqlalchemy import SQLAlchemy
# from app import db
from random import randint

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     nombre = db.Column(db.String(80), unique=True, nullable=False)

class Table: 
    def __init__(self, table_number):
        self.table_number = table_number
        self._products = []
        self.id_client = None
   
    def _generateId(self):
        return randint(0, 99999999)

    def add_product(self, product):
      self._products.append(product)
      return product

    def assign_client(self):
        self.id_client = self._generateId()
        return self.id_client
        
    def clear_table(self):
        self._products = []
        self.id_client = None