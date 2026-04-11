from fastapi import FastAPI
from models import Product
app=FastAPI()
@app.get("/")
def greet():
    return "Hello, to my website"

# list to send dummy data

products=[
    Product(id=1,name="Laptop",brand="asus",description="A high quality laptop",price=45.9,quantity=10),
    Product(id=2,name="Laptop",brand="asus",description="A high quality laptop",price=45.9,quantity=10),
    Product(id=3,name="Laptop",brand="asus",description="A high quality laptop",price=45.9,quantity=10),
    Product(id=4,name="Laptop",brand="asus",description="A high quality laptop",price=45.9,quantity=10),
    Product(id=5,name="Laptop",brand="asus",description="A high quality laptop",price=45.9,quantity=10)
]

 
@app.get("/products")
def get_all_products():
    return products

@app.get("/products/{id}")

def get_product_by_id(id:int):
    for i in range(len(products)):
        if(products[i].id==id):
            return products[i]
        
    return "product with id not present "
        

@app.post("/products")
def add_product_details(product:Product):

    products.append(product)
    return "product added successfully"

@app.put("/product/{id}")
def update_individual_product(id:int,updatedproduct:Product):
    for product in products:
        if product.id==id:
            product.name=updatedproduct.name
            product.brand=updatedproduct.brand
            product.description=updatedproduct.description
            product.price=updatedproduct.price
            product.quantity=updatedproduct.quantity

            return "product updated successfully"   
    return "product with the id does not exits"
            

@app.delete("/product/{id}")
def delete_product_by_id(id:int):
    for  prod in products:
        if prod.id==id:
            products.remove(prod)
            return {
                "message":"Product removed successfully"
                
            }