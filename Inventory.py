import mysql.connector

class Product:
    def __init__(self, id, name, quantity):
        self.id = id
        self.name = name
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="stock"
        )
        self.cursor = self.conn.cursor()

    def add_product(self, product):
        self.cursor.execute("INSERT INTO products VALUES (%s, %s, %s)", (product.id, product.name, product.quantity))
        self.conn.commit()

    def update_product(self, id, quantity):
        self.cursor.execute("UPDATE products SET quantity = %s WHERE id = %s", (quantity, id))
        self.conn.commit()

    def delete_product(self, id):
        self.cursor.execute("DELETE FROM products WHERE id = %s", (id,))
        self.conn.commit()