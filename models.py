from pydantic import BaseModel

class Product(BaseModel):
    id:int
    name :str
    brand:str
    description:str
    price:float
    quantity:int

    











        