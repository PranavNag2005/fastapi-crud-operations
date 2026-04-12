from fastapi import FastAPI,Depends
from models import Product
from database_models import Base
from dbconnection import engine
from dbconnection import session
from database_models import ProductDB
from sqlalchemy.orm import Session 
app=FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    return {"message":"Hello, welcome to the fastapi guys"}

# list to send dummy data

products=[
    Product(id=1,name="Laptop",brand="asus",description="A high quality laptop",price=45.9,quantity=10),
    Product(id=2,name="Laptop",brand="asus",description="A high quality laptop",price=45.9,quantity=10),
    Product(id=3,name="Laptop",brand="asus",description="A high quality laptop",price=45.9,quantity=10),
    Product(id=4,name="Laptop",brand="asus",description="A high quality laptop",price=45.9,quantity=10),
    Product(id=5,name="Laptop",brand="asus",description="A high quality laptop",price=45.9,quantity=10)
]

def _get_db():
    db=session()
    try:
        yield db
    finally:
        db.close()

def __init__db():
    db=session()
    count=db.query(ProductDB).count()
    print(count)
    if count==0:
        for product in products:
            db.add(ProductDB(**product.model_dump()))
        db.commit()
__init__db()
@app.get("/products")
def get_all_products(db:Session=Depends(_get_db)):
    prod_db=db.query(ProductDB).all()
    return prod_db

@app.get("/products/{id}")

def get_product_by_id(id:int,db:Session=Depends(_get_db)):
    # for i in range(len(products)):
    #     if(products[i].id==id):
    #         return products[i]
    prod_db=db.query(ProductDB).filter(ProductDB.id==id).first()    
    if prod_db:
        return prod_db

        
    return {"message":"product with id not found"}
        

@app.post("/products")
def add_product_details(product:Product,db:Session=Depends(_get_db)):
    new_product=ProductDB(**product.model_dump())
    db.add(new_product)
    db.commit()

    
    return "product added successfully"

@app.put("/products/{id}")
def update_individual_product(id:int,updatedproduct:Product,db:Session=Depends(_get_db)):
    # for product in products:
    #     if product.id==id:
    #         product.name=updatedproduct.name
    #         product.brand=updatedproduct.brand
    #         product.description=updatedproduct.description
    #         product.price=updatedproduct.price
    #         product.quantity=updatedproduct.quantity

    #         return "product updated successfully"   
    prod_db=db.query(ProductDB).filter(ProductDB.id==id).first() 
    if prod_db:
        prod_db.brand=updatedproduct.brand
        prod_db.name=updatedproduct.name
        prod_db.description=updatedproduct.description
        prod_db.price=updatedproduct.price
        prod_db.quantity=updatedproduct.quantity
        db.commit()
        return {"message":"product updated successfully."}
    return {
        "message":"product with id not found"
    }
            

@app.delete("/products/{id}")
def delete_product_by_id(id:int,db:Session=Depends(_get_db)):
    prod_db=db.query(ProductDB).filter(ProductDB.id==id).first()
    if prod_db:
        db.delete(prod_db)
        db.commit()
        return {"message":"product deleted successfully"}
    return {"message":"product not found"}
  