Desculpe, parece que houve um erro na sua solicitação. Você mencionou a geração de uma API em Node.js, mas a tarefa original era para um desenvolvedor Python especializado em FastAPI. Vou presumir que você quer uma API em FastAPI com dois endpoints. Aqui está:


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str
    price: float

items = []

@app.post("/items/")
async def create_item(item: Item):
    """Cria um novo item"""
    items.append(item)
    return item

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    """Recupera um item pelo ID"""
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail="Item not found")