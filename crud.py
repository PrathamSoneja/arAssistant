import sqlite3
import pandas as pd

def getInfo(db_name, id):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute(f"""SELECT * FROM items WHERE items.item_id == {id}""")
    df = pd.DataFrame(cur.fetchall(),
                      columns=['item_id', 'item_name', 'item_type', 'item_description', 'item_quantity', 'item_price'])
    conn.commit()
    item_name = df['item_name'][0]
    item_type = df['item_type'][0]
    item_description = df['item_description'][0]
    item_quantity = df['item_quantity'][0]
    item_price = df['item_price'][0]
    return item_name, item_type, item_description, item_quantity, item_price

def getDB(db_name):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute(f"""SELECT * FROM items LIMIT 10""")
    df = pd.DataFrame(cur.fetchall(),
                      columns=['item_id', 'item_name', 'item_type', 'item_description', 'item_quantity', 'item_price'])
    conn.commit()
    return df

def add_item(db_name, id, name, tp, descr, quantity, price):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    my_data = (id, name, tp, descr, quantity, price)
    q = f"INSERT INTO items VALUES (?,?,?,?,?,?)"
    cur.execute(q, my_data)
    conn.commit()
    return 0