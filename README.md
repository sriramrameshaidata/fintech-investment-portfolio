# FinTech: Personalized Investment Portfolio

This project is a personalized investment portfolio analysis tool created as part of the **FinTech Challenge 2024**. It helps users evaluate the performance of a custom stock portfolio compared to the S&P 500 benchmark.

## Features
- Enter custom stock tickers and portfolio weights.
- Fetch real-time data from Yahoo Finance.
- Compare portfolio performance against the S&P 500.
- Download portfolio data as a CSV.

## Demo
[Live Demo](https://fintech-investment-portfolio.streamlit.app)

## How to Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/sriramarameshaidata/fintech-investment-portfolio.git
   cd fintech-investment-portfolio
pip install -r requirements.txt
streamlit run fintech_investment_app.py
Libraries Used
streamlit for the web app.
yfinance for fetching stock market data.
matplotlib and pandas for data visualization and analysis.
Screenshots

License
This project is licensed under the MIT License.


## Use Cases

This app can be valuable in several scenarios:

- **Personal Investment Planning:** Helps individuals plan and simulate potential investment strategies.
- **Comparing Portfolios:** Allows users to compare their custom portfolios against standard benchmarks like the S&P 500.
- **Investment Decision-Making:** Provides insights and analytics to aid in making informed investment decisions.


  ## Technologies Used

- **Streamlit:** An open-source app framework for turning data scripts into shareable web apps.
- **yfinance:** Provides methods for fetching historical market data from Yahoo Finance.
- **matplotlib and pandas:** Used for creating static, interactive, and animated visualizations and data manipulation.
  ## Future Features

Several exciting features are planned to enhance the capabilities of this investment portfolio app:

### Allow Selection of Multiple Benchmarks
- **Flexible Benchmark Comparison:** Users will be able to select from multiple benchmarks such as NASDAQ, Dow Jones, and others via a dropdown or multiselect option.
- **Dynamic Data Fetching:** Leverage `yfinance` to fetch real-time data for these benchmarks, allowing users to perform comprehensive comparisons.

### Display Risk Metrics
- **Volatility:** Show the standard deviation of portfolio returns as a measure of volatility.
- **Sharpe Ratio:** Calculate and display the Sharpe Ratio to assess the return per unit of risk, with a hypothetical risk-free rate (e.g., 3%).
- **Max Drawdown:** Measure and show the largest single drop from peak to bottom in the investment portfolio's value, helping users understand potential losses.


Author
Sriram Ramesh
Contact: sriramramesh.aidata@gmail.com | [LinkedIn](https://www.linkedin.com/in/iamsriramramesh/)
## Screenshots
![Portfolio Dashboard](./screenshots/dashboard.png)
