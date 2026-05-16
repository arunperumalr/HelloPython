import requests

url = "https://fakestoreapi.com/products"

response = requests.get(url)
print("FakeStore API Status Code: ", response.status_code)

data = response.json()
print("\nDisplaying First 5 Products")
print("*"*27)
for product in data[:5]:
    print("Title: ",product["title"])
    print("Price: ",product["price"])
    print("Category: ",product["category"])
    print("-"*40)

print("*"*30)