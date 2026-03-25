from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Modelo
class Order(BaseModel):
    id: int
    product: str
    quantity: int
    status: str = "pending"

orders = []

# Crear pedido
@app.post("/orders")
def create_order(order: Order):
    orders.append(order)
    return {"message": "Order created", "order": order}

# Obtener pedido
@app.get("/orders/{order_id}")
def get_order(order_id: int):
    for order in orders:
        if order.id == order_id:
            return order
    raise HTTPException(status_code=404, detail="Order not found")

# Actualizar estado
@app.put("/orders/{order_id}/status")
def update_status(order_id: int, status: str):
    for order in orders:
        if order.id == order_id:
            order.status = status
            return {"message": "Status updated", "order": order}
    raise HTTPException(status_code=404, detail="Order not found")

# Listar pedidos
@app.get("/orders")
def list_orders():
    return orders