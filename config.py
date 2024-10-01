# List of stock tickers to include in the portfolio
TICKERS = ['AAPL', 'MSFT', 'NVDA']

# Date range for historical data
START_DATE = '2020-01-01'
END_DATE = '2024-09-25'

# Initial investment amount in dollars
INITIAL_INVESTMENT = 10000

# Number of Monte Carlo simulations to run
NUM_SIMULATIONS = 10000

# Investment time horizon in days (e.g., 252 trading days in a year)
TIME_HORIZON = 90

# Risk-free rate for Sharpe Ratio calculation. 0.02 = 2%
RISK_FREE_RATE = 0.045

# Custom weights for each stock (should sum to 1)
# If None, equal weights are assumed unless optimization is used
WEIGHTS = None  # Example: [0.4, 0.3, 0.3]

# Optimization settings
OPTIMIZE = True  # Set to True to optimize the portfolio, False to use provided weights
BALANCED = False  # Set to True for a balanced portfolio, False to maximize Sharpe Ratio
