import yfinance as yf
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Function to calculate cumulative returns
def calculate_cumulative_returns(weights, stock_prices):
    """Calculate cumulative portfolio returns."""
    normalized_prices = stock_prices / stock_prices.iloc[0]  # Normalize prices to start at 1
    portfolio_returns = (normalized_prices * weights).sum(axis=1)
    cumulative_returns = (1 + portfolio_returns.pct_change().fillna(0)).cumprod()
    return cumulative_returns

# Streamlit App
st.title("FinTech: Personalized Investment Portfolio")

# Sidebar for user inputs
st.sidebar.header("Portfolio Configuration")
stocks = st.sidebar.text_input("Enter stock tickers (comma-separated)", "AAPL, MSFT, GOOGL").split(", ")
start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime("2018-01-01"))
end_date = st.sidebar.date_input("End Date", value=pd.to_datetime("2023-01-01"))
weights_input = st.sidebar.text_input("Portfolio Weights (comma-separated)", "0.4, 0.3, 0.3")
optimal_weights = list(map(float, weights_input.split(", ")))

if len(optimal_weights) != len(stocks):
    st.error("The number of weights must match the number of stocks!")
    st.stop()

try:
    # Fetch stock data
    st.write("Fetching stock data...")
    stock_prices = yf.download(stocks, start=start_date, end=end_date)['Adj Close']
    stock_prices = stock_prices.dropna()

    # Fetch benchmark data
    benchmark_data = yf.download("^GSPC", start=start_date, end=end_date)['Adj Close']
    benchmark_cumulative_returns = (1 + benchmark_data.pct_change().fillna(0)).cumprod()

    # Calculate portfolio cumulative returns
    portfolio_cumulative_returns = calculate_cumulative_returns(optimal_weights, stock_prices)

    # Plot Portfolio vs Benchmark
    st.subheader("Portfolio vs Benchmark Performance")
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(portfolio_cumulative_returns, label="Portfolio", color='blue')
    ax.plot(benchmark_cumulative_returns, label="Benchmark (S&P 500)", color='orange')
    ax.set_title("Portfolio vs Benchmark Performance")
    ax.set_xlabel("Date")
    ax.set_ylabel("Cumulative Returns")
    ax.legend()
    ax.grid()
    st.pyplot(fig)

    # Evaluate performance metrics
    portfolio_final_return = (portfolio_cumulative_returns.iloc[-1] - 1).item()
    benchmark_final_return = (benchmark_cumulative_returns.iloc[-1] - 1).item()  

    st.subheader("Performance Metrics")
    st.write(f"**Final Portfolio Return:** {portfolio_final_return * 100:.2f}%")
    st.write(f"**Final Benchmark Return:** {benchmark_final_return * 100:.2f}%")
    st.write(f"**Portfolio Weights:** {optimal_weights}")

    # Add download button for results
    st.download_button(
        label="Download Portfolio Data as CSV",
        data=stock_prices.to_csv().encode('utf-8'),
        file_name='portfolio_data.csv',
        mime='text/csv'
    )

except Exception as e:
    st.error(f"An error occurred: {e}")
