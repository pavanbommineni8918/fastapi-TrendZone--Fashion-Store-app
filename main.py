from fastapi import FastAPI, HTTPException, Query, status
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI(title=" TrendZone Fashion Store API")

# -----------------------------
# In-memory database
# -----------------------------
products = []
cart = []
orders = []

# -----------------------------
# Pydantic Models
# -----------------------------
class Product(BaseModel):
    id: int
    name: str = Field(..., min_length=2)
    category: str
    price: float = Field(..., gt=0)
    stock: int = Field(..., ge=0)

class ProductCreate(BaseModel):
    name: str
    category: str
    price: float
    stock: int

class CartItem(BaseModel):
    product_id: int
    quantity: int = Field(..., gt=0)

class Order(BaseModel):
    id: int
    items: List[CartItem]
    total: float
    status: str

# -----------------------------
# Helper Functions
# -----------------------------
def find_product(product_id: int):
    for p in products:
        if p["id"] == product_id:
            return p
    return None

def calculate_total(items: List[CartItem]):
    total = 0
    for item in items:
        product = find_product(item.product_id)
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        total += product["price"] * item.quantity
    return total

def filter_products(keyword=None, category=None):
    result = products
    if keyword:
        result = [p for p in result if keyword.lower() in p["name"].lower()]
    if category:
        result = [p for p in result if p["category"].lower() == category.lower()]
    return result

# -----------------------------
# Day 1: GET APIs
# -----------------------------
@app.get("/")
def home():
    return {"message": "Welcome to Fashion Store API"}

@app.get("/products")
def get_all_products():
    return products

@app.get("/products/count")
def product_count():
    return {"total_products": len(products)}

@app.get("/products/{product_id}")
def get_product(product_id: int):
    product = find_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# -----------------------------
# Day 2: POST + Validation
# -----------------------------
@app.post("/products", status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate):
    new_product = product.dict()
    new_product["id"] = len(products) + 1
    products.append(new_product)
    return new_product

# -----------------------------
# Day 4: CRUD Operations
# -----------------------------
@app.put("/products/{product_id}")
def update_product(product_id: int, updated: ProductCreate):
    product = find_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    product.update(updated.dict())
    return product

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    product = find_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    products.remove(product)
    return {"message": "Product deleted"}

# -----------------------------
# Day 5: Multi-Step Workflow
# Cart → Order → Checkout
# -----------------------------
@app.post("/cart")
def add_to_cart(item: CartItem):
    product = find_product(item.product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    if product["stock"] < item.quantity:
        raise HTTPException(status_code=400, detail="Not enough stock")

    cart.append(item)
    return {"message": "Item added to cart", "cart": cart}

@app.get("/cart")
def view_cart():
    return cart

@app.post("/order")
def place_order():
    if not cart:
        raise HTTPException(status_code=400, detail="Cart is empty")

    total = calculate_total(cart)

    new_order = {
        "id": len(orders) + 1,
        "items": cart.copy(),
        "total": total,
        "status": "Placed"
    }

    orders.append(new_order)
    cart.clear()

    return new_order

@app.put("/order/{order_id}/checkout")
def checkout(order_id: int):
    for order in orders:
        if order["id"] == order_id:
            order["status"] = "Completed"
            return order

    raise HTTPException(status_code=404, detail="Order not found")

# -----------------------------
# Day 6: Advanced APIs
# Search, Sorting, Pagination
# -----------------------------
@app.get("/products/search")
def search_products(
    keyword: Optional[str] = Query(None),
    category: Optional[str] = Query(None),
    sort_by: Optional[str] = Query(None),
    page: int = 1,
    limit: int = 5
):
    result = filter_products(keyword, category)

    if sort_by == "price":
        result = sorted(result, key=lambda x: x["price"])
    elif sort_by == "-price":
        result = sorted(result, key=lambda x: x["price"], reverse=True)

    start = (page - 1) * limit
    end = start + limit

    return {
        "page": page,
        "limit": limit,
        "total": len(result),
        "data": result[start:end]
    }
