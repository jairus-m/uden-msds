import pandas as pd

def loadInvestments(path: str):
    """
    Loads investment options from CSV file and returns a list of tuples.
    Args:
        path (str): The filename of the CSV containing investment options.
    Returns:
        list of tuples: A list of tuples where each tuple contains:
            - investment_region (str): The name of the investment (state).
            - avg_home_price (int): The cost of the investment (ZHVI).
            - estimated_return (float): The estimated return on investment.
    """
    df = pd.read_csv(path)
    # format data!
    df = (df.loc[1:, ['RegionName', 'Zhvi', '10Year']] 
          .reset_index(drop=True)
          .rename(columns={
              'RegionName': 'investment_region', 
              'Zhvi': 'avg_home_price', 
              '10Year': 'avg_return'
          })
          .assign(
              estimated_return=lambda x: x['avg_home_price'] * (x['avg_return'])
          )
          .drop(columns=['avg_return'])
    )
    
    # convert df to a list of tuples
    data = list(df.itertuples(index=False, name=None))
    
    return df, data

def optimizeInvestments(investment_data: list, budget: int):
    """
    Optimize the selection of investments to maximize 
    return on investment using dynamic programming.
    Args:
        investment_data (list of tuples): A list of investment options, where each tuple contains:
            - investment_region (str): The name of the investment (state).
            - avg_home_price (int): The cost of the investment.
            - estimated_return (float): The estimated return on investment.
        budget (int): The maximum amount of money available to invest.
    Returns:
        tuple: 
            - optimal_roi (float): The maximum return on investment possible with the given budget
            - selected_investments (list of str): The list of investments (names) that were selected to achieve this optimal return
            - total_cost (int) : Sum of the cost to pay for each investment
    """
    n = len(investment_data)

    # initialize table w/ 0s
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    
    # iterature thru each investment/budget combo
    for i in range(1, n + 1):
        name, cost, roi = investment_data[i - 1]
        for j in range(1, budget + 1):
            # check if cost is <= current budget
            if cost <= j:
                # update max value
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost] + roi)
            else:
                # leave alone
                dp[i][j] = dp[i - 1][j]
    
    # traceback to find the selected investments from dp table
    selected_investments = []
    # track total cost
    total_cost = 0
    i, j = n, budget
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            name, cost, roi = investment_data[i - 1]
            selected_investments.append(name)
            total_cost += increment_round(cost, 1000) # round up cost of house to nearest 1000
            j -= cost
        i -= 1
    
    optimal_roi = dp[-1][-1]
    
    return optimal_roi, selected_investments[::-1], total_cost

def increment_round(p: int, i: int):
    """
    Round a number up by a preselected increment value.
    Args:
        p (int) : integer
        i (int) : increment value
    Returns:
        int : rounded value
    """
    # we went over this in class!
    answer = ((p // i) + 1) * i

    return answer

if __name__ == "__main__":
    # load data
    df, investments = loadInvestments('state_zhvi_summary_allhomes.csv')

    # Find the best way to invest $ 1,000,000 by buying up to one house in any given state. 
    # Round up the value of the house to the nearest $1000. 
    
    budget = 1000000
    
    # run optimization
    optimal_roi, selected_investments, total_cost = optimizeInvestments(investments, budget)
    
    # results
    print('\n')
    print(f'Budget: ${budget:,.2f}')
    print("Selected Investments:", selected_investments)
    print(f'Spent: ${total_cost:,.2f}')
    print(f"Est. Optimal ROI to the nearest 1000: ${increment_round(optimal_roi, 1000):,.2f}")
    print('\n')

    for investment in selected_investments:
        p_cost = df.loc[df['investment_region'] == investment, ['avg_home_price']].values[0][0]
        p_return = df.loc[df['investment_region'] == investment, ['estimated_return']].values[0][0]
        print(f'Investment: {investment}')
        print(f'House cost to the nearest 1000: ${increment_round(p_cost, 1000):,.2f}')
        print(f'House est. return to the nearest 1000: ${increment_round(p_return, 1000):,.2f}')
        print('--- ' * 13)

# TERMINAL OUTPUT
#
# Budget: $1,000,000.00
# Selected Investments: ['Michigan', 'Tennessee', 'Colorado', 'Nevada']
# Spent: $996,000.00
# Est. Optimal ROI to the nearest 1000: $50,000.00
# 
# 
# Investment: Michigan
# House cost to the nearest 1000: $153,000.00
# House est. return to the nearest 1000: $7,000.00
# --- --- --- --- --- --- --- --- --- --- --- --- --- 
# Investment: Tennessee
# House cost to the nearest 1000: $168,000.00
# House est. return to the nearest 1000: $6,000.00
# --- --- --- --- --- --- --- --- --- --- --- --- --- 
# Investment: Colorado
# House cost to the nearest 1000: $381,000.00
# House est. return to the nearest 1000: $22,000.00
# --- --- --- --- --- --- --- --- --- --- --- --- --- 
# Investment: Nevada
# House cost to the nearest 1000: $294,000.00
# House est. return to the nearest 1000: $16,000.00