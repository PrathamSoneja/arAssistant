from typing import Union

import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from crud import *
from qna_model import *

configfile = 'config.json'
db = 'identifier.sqlite'

app = FastAPI()


class Item(BaseModel):
    item_name: str
    item_type: Union[str, None] = None
    item_description: str
    item_quantity: int
    item_price: int


@app.get("/")
async def read_root():
    return {"Message": "Hello, Customer"}

#@app.get("/items/")
#async def read_df():
#    df = getDB(db)
#    return df.to_dict()

@app.get("/items/{item_id}/")
async def read_item(item_id: int):
    item_name, item_type, item_description, item_quantity, item_price = getInfo(db, item_id)
    return {"item_id": str(item_id), "item_name": str(item_name), "item_type": str(item_type), "item_desc": str(item_description), "quantity": str(item_quantity), "price": str(item_price)}

@app.get("/items/{item_id}/{question}/")
async def ans_ques(item_id: int, question: str):
    question = f"{question}?"
    item_name, item_type, item_description, item_quantity, item_price = getInfo(db, item_id)
    outputs = bertModel(configfile, question, item_description)
    count = 0
    while 'score' not in outputs:
        outputs = bertModel(configfile, question, item_description)
        count=count+1
        if count >= 5:
            raise HTTPException(status_code=404, detail="Error in fetching results")

    return {"question": question, "probability": str(np.round(outputs['score']*100, 3)), "answer": str(outputs['answer'])}

@app.post("/item/")
async def create_item(item: Item):
    df = getDB(db)
    id = len(df)+101
    add_item(db, id, item.item_name, item.item_type, item.item_description, item.item_quantity, item.item_price)
    return {
        "status": "SUCCESS",
        "data": item
    }