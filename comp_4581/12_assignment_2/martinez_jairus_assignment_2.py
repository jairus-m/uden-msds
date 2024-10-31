import pandas as pd
import numpy as np

def load_data():
    """
    Loads and formats the csv files from securities.csv 
    and the prices-split-adjusted.csv file. 
    Args:
        None
    Returns
        tuple: df_prices, df_securities
    """
    # read in and format df_prices
    df_prices = pd.read_csv('prices-split-adjusted.csv')
    df_prices = df_prices[['date', 'symbol', 'close']]

    # read in and format df_securities
    df_securities = pd.read_csv('securities.csv')
    df_securities = df_securities[['Ticker symbol', 'Security']]
    df_securities.columns = ['ticker', 'name']

    return df_prices, df_securities

def max_profiit_dac(A, low=0, high=None):
    """
    This function recursively looks for the max difference
    in an array via DAC. 
    Args:
        A (array-like) : stock closing prices
        low (int) : lowest closing price
        high (int) : highest closing price
    """
    if high is None:
        high = len(A) - 1

    # base case: if the array has only one element
    if low == high:
        return A[low], A[low], 0  

    # base case: if the array has two elements
    if high == low + 1:
        min_val = min(A[low], A[high])
        max_val = max(A[low], A[high])
        return min_val, max_val, max_val - min_val

    # divide
    mid = (low + high) // 2

    # conquer
    minLeft, maxLeft, maxDiffLeft = max_profiit_dac(A, low, mid)
    minRight, maxRight, maxDiffRight = max_profiit_dac(A, mid + 1, high)

    # combine
    maxDiffAcross = maxRight - minLeft

    maxDiff = max(maxDiffLeft, maxDiffRight, maxDiffAcross)

    # Determine overall min and max values
    overall_min = min(minLeft, minRight)
    overall_max = max(maxLeft, maxRight)

    return overall_min, overall_max, maxDiff

df_prices, df_securities = load_data()

if __name__ == '__main__':
    # initialize base nums
    max_diff = 0
    most_min = 0
    most_max = 0
    best_ticker = None

    # loop thru all tickers
    for i in range(df_securities.shape[0]):

        ticker = df_securities.iloc[i]['ticker']
        
        df = df_prices.loc[df_prices['symbol'] == ticker, ['date', 'close']]

        # make sure ticker does not return 0 data
        if df.shape[0] != 0:
            minimum, maximum, diff = max_profiit_dac(np.array(df['close']))

            # constantly look for best diff value and save values outside of loop
            if diff > max_diff:
                max_diff = diff
                most_min = minimum
                most_max = maximum
                best_ticker = ticker
            else:
                pass
        else:
            pass
    
    # get the final dates / company name
    minDate = df_prices.loc[(df_prices['close'] == most_min) & (df_prices['symbol'] == best_ticker), ['date']].values[0][0]
    maxDate = df_prices.loc[(df_prices['close'] == most_max) & (df_prices['symbol'] == best_ticker), ['date']].values[0][0]
    security = df_securities.loc[df_securities['ticker'] == best_ticker, 'name'].tolist()[0]

    print(f'Best stock to buy: {security} on {minDate} and sell on {maxDate} with profit of ${max_diff:.2f}')

# TERMINAL OUTPUT

# Best stock to buy: Priceline.com Inc on 2010-06-09 and sell on 2016-11-08 with profit of $1402.94