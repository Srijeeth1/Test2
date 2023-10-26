import csv

csv_file="customer_orders.csv"
orders=[]
with open(csv_file,mode="r")as file:
    reader=csv.DictReader(file)
    for row in reader:
        order={
            "Orderid": int(row["Orderid"]),
            "product":str(row["product"]),
            "quantity":int(row["quantity"]),
            "price":float(row["price"])
    }
    orders.append(order)
    product_data[product]["TotalQuantityOrdered"]+=quantity
    product_data[product]["TotalRevenue"]+=quantity*price
total_revenue=sum(order["quantity"]*order["price"]for order in orders)
print("Total Revenue: $",total_revenue)
most_popular_product=max(quantity)
print("Most Popular Product",most_popular_product)
average_price=total_price/num_orders
print("average price",average_price)
summary_csv_file="product_summary.csv"
with open(summary_csv_file,mode="w",newline="")as summary_file:
    fieldnames=["product","TotalQuantityOrdered","TotalRevenue"]
    writer= csv.Dictwriter(summary_file,fieldnames=fieldnames)
    writer.writeheader()
    for product, data in product_data.items():
        writer.writerow({
            "product":product,
            "TotalQuantityOrdered":data["TotalQuantityOrdered"],
            "TotalRevenue":data["TotalRevenue"]
        })
highest_total_revenue=max(total_revenue)
print("Highest Total Revenue",highest_total_revenue)
print("first order",orders[0])    

    
            
        
