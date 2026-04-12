from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,Float,String
Base=declarative_base()  # this is the parent class for all the tables

class ProductDB(Base):
    __tablename__="product"
    id= Column(Integer,primary_key=True,index=True)
    name = Column(String)
    brand=Column(String)
    description=Column(String)
    price=Column(Float)
    quantity=Column(Integer)