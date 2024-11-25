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

## Improve Visual Appeal

To make the user interface more engaging and easier to use, the following visual enhancements are planned:

### Customize Plot
- **Interactive Charts:** Implement charts using `plotly` to enable interactive features such as zooming and tooltips.
- **Enhanced Aesthetics:** Improve the visual presentation with user-friendly labels, legends, and a modern color palette.

### Experiment with Grid Styles
- **Gridlines:** Introduce both minor and major gridlines to the charts for better readability and precision in data visualization, utilizing either `matplotlib` or `plotly`.

## Demo Enhancements

To help new users understand how to make the most of the FinTech Investment Portfolio app, the following demo materials will be provided:

## Optimize Deployment

To ensure that the FinTech Investment Portfolio app is always running the latest version without manual intervention, the following CI/CD processes will be implemented:

## Promotion

To increase visibility and user engagement of the FinTech Investment Portfolio app, the following promotional activities will be undertaken:

### Share on Platforms
- **Social Media and Blogs:** The project will be shared on platforms like LinkedIn, Twitter, and Medium, including links to the GitHub repository and the live demo to attract a broader audience.
- **Community Engagement:** Participation in relevant online communities such as Streamlit forums and Reddit r/learnprogramming will be increased to gain feedback and drive improvements.

### Highlight Unique Features
- **Feature Showcases:** Regular posts will highlight how the app allows users to personalize and analyze their investment portfolios with ease, demonstrating the app's value in investment planning and analysis.


### Set Up GitHub Actions for CI/CD
- **Automated Deployment:** A GitHub Actions workflow will be configured to automatically deploy the application to Streamlit Cloud upon any commits to the `main` branch.
- **Workflow File:** A `.github/workflows/deploy.yml` file will be added to the repository to manage the integration with Streamlit Cloud.


### Create a Video Walkthrough
- **Video Tutorial:** A video will be created to demonstrate the setup process, how to customize portfolios, and how to interpret the comparison results. This video will be embedded directly into the README to provide an easy-to-follow visual guide.

### Add More Screenshots
- **Diverse App States:** Additional screenshots will be captured to showcase different states of the app, including successful portfolio setups and common error scenarios, such as mismatched weights and stocks.


Author
Sriram Ramesh
Contact: sriramramesh.aidata@gmail.com | [LinkedIn](https://www.linkedin.com/in/iamsriramramesh/)
## Screenshots
![Portfolio Dashboard](dashboard.png)



