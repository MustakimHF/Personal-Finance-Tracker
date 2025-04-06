import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

# Function to load and clean data
def load_data():
    try:
        df = pd.read_csv("transactions.csv")  # Ensure 'transactions.csv' is in the same directory
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')  # Ensure Date column is datetime
        return df
    except FileNotFoundError:
        print("Error: 'transactions.csv' not found.")
        exit()

# Function for basic analysis
def analyze_data(df):
    budgets = {'Food': 500, 'Rent': 1000, 'Transport': 200}
    df_grouped = df.groupby('Category')['Amount'].sum()
    
    for category, budget in budgets.items():
        spent = df_grouped.get(category, 0)
        print(f"In {category}, you spent ${spent}. Your budget is ${budget}.")
        if spent > budget:
            print(f"Alert: You exceeded your budget in {category} by ${spent - budget}")
    
    return df_grouped

# Function to visualize spending using Matplotlib
def plot_pie_chart(df_grouped):
    df_grouped.plot(kind='pie', y='Amount', autopct='%1.1f%%', legend=False)
    plt.title("Spending by Category")
    plt.show()

# Function to visualize spending over time using Plotly
def plot_line_chart(df):
    fig = px.line(df, x='Date', y='Amount', color='Category', title='Spending Over Time')
    fig.show()

# Dash App for Interactive Visualization
def create_dash_app(df):
    # Dash App with pastel colors
    pastel_colors = ['#FFB5E8', '#FF9CEE', '#B28DFF', '#85E3FF', '#BFFCC6', '#FFFFD1', '#FFABAB']

    app = Dash(__name__)

    app.layout = html.Div([
        html.H1("Personal Finance Tracker", style={'textAlign': 'center', 'color': '#6B705C'}),
        dcc.DatePickerRange(
            id='date-picker',
            start_date=min(df['Date']),
            end_date=max(df['Date']),
            style={'padding': '10px'}
        ),
        dcc.Graph(id='spending-graph', style={'margin-top': '20px'}),
        html.Footer("Finance Tracker by [Your Name]", style={'textAlign': 'center', 'padding': '20px', 'color': '#6B705C'})
    ])

    @app.callback(
        Output('spending-graph', 'figure'),
        [Input('date-picker', 'start_date'), Input('date-picker', 'end_date')]
    )
    def update_graph(start_date, end_date):
        filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
        fig = px.pie(
            filtered_df,
            values='Amount',
            names='Category',
            title='Spending Breakdown',
            color_discrete_sequence=pastel_colors
        )
        fig.update_layout(
            title_font_color='#6B705C',
            paper_bgcolor='#FAF3E0',
            font_color='#6B705C'
        )
        return fig

    return app

# Main Function
if __name__ == "__main__":
    # Load data
    df = load_data()

    # Analyze and print results
    df_grouped = analyze_data(df)

    # Visualize data using Matplotlib and Plotly
    plot_pie_chart(df_grouped)
    plot_line_chart(df)

    # Run Dash App
    app = create_dash_app(df)
    app.run_server(debug=True)
