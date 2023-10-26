
# Online Python - IDE, Editor, Compiler, Interpreter
import csv
import random

def generate_random_entries():
    Orderid=random.randint(1,1000)
    product = f"Widget{random.randint(1,10)}"
    quantity =random.randint(1,10)
    price =round(random.uniform(10.0,100.0),2)
    return[Orderid,product,quantity,price]
    
csv_file="customer_orders.csv"

with open(csv_file,mode="w",newline="")as file:
    writer=csv.writer(file)
    writer.writerow(["Orderid","Widget","quantity","price"])
    for _ in range(100):
            Orderid_data = generate_random_entries()
            writer.writerow(Orderid_data)
            print(Orderid_data)
            
         
           
        
        # TODO: write code...

    