import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL (Demo website for web scraping)
url = "https://books.toscrape.com/"

# Send HTTP request
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all product containers
    products = soup.find_all("article", class_="product_pod")

    # List to store product data
    product_data = []

    for product in products:

        # Product Name
        name = product.h3.a["title"]

        # Product Price
        price = product.find("p", class_="price_color").text

        # Product Rating
        rating = product.find("p")["class"][1]

        # Save data
        product_data.append({
            "Product Name": name,
            "Price": price,
            "Rating": rating
        })

    # Convert to DataFrame
    df = pd.DataFrame(product_data)

    # Save to CSV
    df.to_csv("products.csv", index=False)

    print("Data Successfully Scraped!")
    print(df)

else:
    print("Failed to connect to the website.")