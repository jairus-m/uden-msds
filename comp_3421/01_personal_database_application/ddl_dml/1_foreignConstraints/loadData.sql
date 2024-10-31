DROP DATABASE IF EXISTS dash;
CREATE DATABASE IF NOT EXISTS dash;
USE dash;

SHOW TABLES;

-- Create User table if it does not exist
CREATE TABLE IF NOT EXISTS Users (
    user_id INT PRIMARY KEY,
    name VARCHAR(255),
    subscription_type VARCHAR(255),
    date_created DATE
);

-- Create Subscription table if it does not exist
CREATE TABLE IF NOT EXISTS Subscriptions (
    sub_id INT PRIMARY KEY,
    user_id INT,
    payment_interval VARCHAR(255),
    payment_cost INT,
    purchase_date DATE NULL,
    end_date DATE NULL,
    status VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- Create Activities table if it does not exist
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

load data local infile "big_data/users.csv" into table Users
	fields terminated by ','
    lines terminated by '\n'
    ignore 1 lines
    ;

load data local infile "big_data/subscriptions.csv" into table Subscriptions
	fields terminated by ','
    lines terminated by '\n'
    ignore 1 lines
    SET end_date = NULLIF(@end_date, '')
    ;
    
load data local infile "big_data/activities.csv" into table Activities
	fields terminated by ','
    lines terminated by '\n'
    ignore 1 lines
    ;



