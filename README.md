💸 Personal Finance Tracker
A simple, interactive app to help you track your spending, stay on budget, and get a better sense of where your money goes. Built with Python, Dash, and Plotly.

✨ What It Does
Loads your transaction data from a CSV file

Groups and analyzes expenses by category

Compares spending to preset budgets (and warns you if you're over)

Lets you explore your spending visually with pie and line charts

Includes an interactive dashboard where you can filter by date

🖼️ Quick Preview
(Add screenshots or a short GIF of the dashboard here to show off the UI)

🧰 Tools & Libraries
Python

Pandas for data wrangling

Matplotlib and Plotly for graphs

Dash for the web dashboard

🚀 How to Run It
Clone this repo

bash
Copy
Edit
git clone https://github.com/yourusername/personal-finance-tracker.git
cd personal-finance-tracker
Install the dependencies

bash
Copy
Edit
pip install -r requirements.txt
(Or manually: pip install pandas matplotlib plotly dash)

Add your data

Make sure you have a file called transactions.csv in the project folder.
It should have three columns:

yaml
Copy
Edit
Date,Category,Amount
2025-01-05,Food,23.5
2025-01-10,Rent,1200
2025-01-12,Transport,45.9
Run the app

bash
Copy
Edit
python finance_tracker.py
Then open your browser and go to http://127.0.0.1:8050/.

📊 Budgets & Alerts
Right now, the app checks for overspending in these categories:

Food: $500

Rent: $1000

Transport: $200

You can change these values in the analyze_data function to fit your own goals.
