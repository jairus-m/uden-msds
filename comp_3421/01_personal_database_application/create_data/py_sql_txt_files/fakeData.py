"""Module to create synthetic data for COMP 3421 PDA"""

from random import randint, choices, choice
from datetime import datetime, timedelta
import logging
import pandas as pd

# basic logging and formatting
logging.basicConfig(format='fakeData - %(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

def timing_decorator(func):
    """Times any function that it's wrapped around"""
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()

        elapsed_time = end_time - start_time
        logging.info(f"{func.__name__}(): {elapsed_time.total_seconds():.2f}s.")
        return result

    return wrapper

@timing_decorator
def create_users(num_records: int, year_start: int, year_end:int , percent_free: float):
    """
    Creates synthetic users for Users table within PDA.

    SQL Schema:
        CREATE TABLE IF NOT EXISTS Users (
        user_id INT PRIMARY KEY,
        name VARCHAR(255),
        subscription_type VARCHAR(255),
        date_created DATE
        );

    Params:
        num_records: how many unique users
        year_start: year to start date for range of creation
        year_end: year to end date for range of creation
        percent_free: percent of users who hava a 'free' subscription
    Returns:
        df_users : pd.DataFrame
    """
    users_data = []

    # generate and insert num_records users into the DataFrame
    for user_id in range(1, num_records + 1):
        name = f'user{user_id}'
        
        # determine subscription type based on the specified percentages
        subscription_type = 'free' if randint(1, 100) <= percent_free else 'premium'
        
        # generate a random date between 2017 and 2024
        date_created = datetime(year_start, 1, 1) + timedelta(days=randint(0, (year_end - year_start) * 365))

        # append the generated data to a temporary DataFrame
        users_entry = {
            'user_id': user_id,
            'name': name,
            'subscription_type': subscription_type,
            'date_created': date_created.strftime('%Y-%m-%d')
        }

        users_data.append(users_entry)
    
    df_users = pd.DataFrame(users_data)
    return df_users

@timing_decorator
def create_subsciptions(subscribed_users: pd.DataFrame):
    """
    Creates synthetic subscriptions data for Subscriptions table wihtin PDA.

    SQL Schema:
        CREATE TABLE IF NOT EXISTS Subscriptions (
        sub_id INT PRIMARY KEY,
        user_id INT,
        payment_interval VARCHAR(255),
        payment_cost INT,
        purchase_date DATE NULL,
        end_date DATE NULL,
        status VARCHAR(255),ßß
        FOREIGN KEY (user_id) REFERENCES Users(user_id)
        );

    Params:
        subscribed_users: dataframe contaiing subscribed users only
    Returns:
        df_subscriptions: pd.Dataframe
    """
    subscriptions_data = []

    for i in subscribed_users.index:
        user_id = subscribed_users.loc[i, 'user_id']
        sub_id = int(f'5{user_id}')
        payment_interval = choices(['monthly', 'semi-annual', 'annual'], 
                                weights=[.70, .10, .20])[0]
        
        if payment_interval == 'annual':
            payment_cost = 120
        elif payment_interval == 'semi-annual':
            payment_cost = 65
        else:
            payment_cost = 11

        purchase_date = pd.to_datetime(subscribed_users.loc[i, 'date_created']) + timedelta(days=randint(0, 365))

        status = 'active'
        end_date = pd.NA

        # append the generated data to a temporary DataFrame
        subscriptions_entry = {
            'sub_id': sub_id,
            'user_id': user_id,
            'payment_interval': payment_interval,
            'payment_cost': payment_cost,
            'purchase_date': purchase_date.strftime('%Y-%m-%d'),
            'end_date': end_date,
            'status': status
        }

        subscriptions_data.append(subscriptions_entry)

        df_subscribers = pd.DataFrame(subscriptions_data)

    return df_subscribers 

@timing_decorator
def create_activities(df_users: pd.DataFrame):
    """
    Create Activities table.

    CREATE TABLE IF NOT EXISTS Activities (
    actv_id INT PRIMARY KEY,
    user_id INT,
    actv_name VARCHAR(255),
    actv_type VARCHAR(255),
    avg_speed INT,
    duration INT,
    heartrate INT,
    upload_date DATE,  -- Added missing comma here
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
    );

    Params:
        df_users: dataframe containing all user data
    Returns:
        df_activities: pd.DataFrame
    """
    activities_data = []

    for user_id in df_users['user_id']:
        num_activities = randint(1, 100)

        for i in range(num_activities):
            actv_id = int(f'{user_id}0{i}')
            actv_type = choice(['Running', 'Cycling', 'Hiking', 'Gym', 'Swimming', 'RockClimbing'])
            actv_name = f'{actv_type} Activity {randint(1, 100)}'

            if actv_type == 'Running':
                avg_speed = randint(1, 7)
            elif actv_type == 'Cycling':
                avg_speed = randint(10, 21)
            elif actv_type == 'RockClimbing' or actv_type == 'Gym':
                avg_speed = 0
            else:
                avg_speed = randint(1, 3)

            if actv_type == 'Running' or actv_type == 'RockClimbing' or actv_type == 'Gym':
                duration = randint(15, 120)
            elif actv_type == 'Cycling':
                duration = randint(60, 360)
            else:
                duration = randint(15, 45)

            heartrate = randint(100, 160)

        
            upload_date = pd.to_datetime(df_users.loc[i, 'date_created']) + timedelta(days=randint(0, 4 * 365))

            activity_entry = {
                'actv_id': actv_id,
                'user_id': user_id,
                'actv_name': actv_name,
                'actv_type': actv_type,
                'avg_speed': avg_speed,
                'duration': duration,
                'heartrate': heartrate,
                'upload_date': upload_date.strftime('%Y-%m-%d')
            }

            activities_data.append(activity_entry)

    df_activities = pd.DataFrame(activities_data)
    return df_activities

@timing_decorator
def main(num_users: int, percent_free: int):
    """
    Exports 3 csv files corresponding to df_users, df_subscriptions, 
    and df_activities. 
    Params:
        num_users: number of users which dictates Subscribers/Activities record lengths
        percent_free: percent of users with a "free" account
    Returns:
        None
    """
    try:
        logging.info('Creating users table...')
        df_users = create_users(num_users, 2017, 2022, percent_free)
        subscribed_users = df_users.loc[df_users['subscription_type'] == 'premium', ['user_id', 'date_created']]
        
        logging.info('Creating Subscriptions table...')
        df_subscribers = create_subsciptions(subscribed_users)

        logging.info('Creatng activities table...')
        df_activities = create_activities(df_users.loc[:, ['user_id', 'date_created']])

        logging.info('Exporting data...')
        df_users.to_csv('data/users.csv', index=False)
        df_subscribers.to_csv('data/subscriptions.csv', index=False)
        df_activities.to_csv('data/activities.csv', index=False)

        logging.info('Export complete')
    except Exception as e:
        logging.error(f'Error: {e}')
        

if __name__ == '__main__':
    main(num_users=10000, percent_free=65)
