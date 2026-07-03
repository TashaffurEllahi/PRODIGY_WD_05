# PRODIGY_WD_05
Web Scraping Product Information
# Product Information Web Scraper

## Task Overview

This project is a part of my **Software Development Internship**.

The program extracts product information from an online e-commerce website using Python and stores the data in a CSV file.

## Technologies Used

* Python
* Requests
* BeautifulSoup (bs4)
* Pandas
* CSV

## Features

* Connects to an online e-commerce website.
* Extracts product names.
* Extracts product prices.
* Extracts product ratings.
* Stores the extracted data in a CSV file.
* Displays the scraped data in the terminal.

## Project Files

* `main.py` – Python source code.
* `products.csv` – Stores the scraped product information.
* `README.md` – Project documentation.

## Installation

Open the terminal in Visual Studio Code and run the following command to install the required libraries:

```bash
pip install requests beautifulsoup4 pandas
```

## Run the Program

After installing the libraries, run the Python program:

```bash
python main.py
```

> **Note:** If `python` does not work on your system, use:

```bash
python3 main.py
```

## Output

After running the program:

* Product information will be displayed in the terminal.
* A file named `products.csv` will be created automatically in the project folder.

## Viewing the CSV File in Visual Studio Code

To view `products.csv` in a spreadsheet-style table:

1. Open the **Extensions** tab in VS Code (`Ctrl + Shift + X`).
2. Search for **Edit CSV**.
3. Install the **Edit CSV** extension.
4. Open `products.csv`.
5. Right-click inside the file and select **Edit CSV**, or press **Ctrl + Shift + P** and choose **Edit CSV: Open CSV Editor**.

The product data will be displayed in a clean table format.

## Sample Output

| Product Name         | Price  | Rating |
| -------------------- | ------ | ------ |
| A Light in the Attic | £51.77 | Three  |
| Tipping the Velvet   | £53.74 | One    |
| Soumission           | £50.10 | One    |

## Learning Outcomes

Through this project, I learned:

* Web scraping using Python.
* Sending HTTP requests with the Requests library.
* Parsing HTML using BeautifulSoup.
* Organizing data with Pandas.
* Saving data in CSV format.
* Viewing CSV files in Visual Studio Code using the **Edit CSV** extension.

---

**Software Development Internship – Task 3**
