SET GLOBAL local_infile=1;

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

load data local infile "data/users.csv" into table Users
	fields terminated by ','
    lines terminated by '\n'
    ignore 1 lines
    ;

load data local infile "data/subscriptions.csv" into table Subscriptions
	fields terminated by ','
    lines terminated by '\n'
    ignore 1 lines
    SET end_date = NULLIF(@end_date, '')
    ;
    
load data local infile "data/activities.csv" into table Activities
	fields terminated by ','
    lines terminated by '\n'
    ignore 1 lines
    ;

SHOW TABLES;

SELECT 'running describe Users' AS '';
DESCRIBE Users;

SELECT 'running describe Subscriptions' AS '';
DESCRIBE Subscriptions;

SELECT 'running describe Activities' AS '';
DESCRIBE Activities;

SELECT 'running select * from Users LIMIT 10' AS '';
SELECT * FROM Users LIMIT 10;

SELECT ' running SELECT COUNT(*) FROM Users;' AS '';
SELECT COUNT(*) FROM Users;

SELECT 'running select * from Subscriptions LIMIT 10' AS '';
SELECT * FROM Subscriptions LIMIT 10;

SELECT 'running SELECT COUNT(*) FROM Subscriptions;' AS '';
SELECT COUNT(*) FROM Subscriptions;

SELECT 'running select * from Activities LIMIT 10' AS '';
SELECT * FROM Activities LIMIT 10;

SELECT 'running SELECT COUNT(*) FROM Activities;' AS '';
SELECT COUNT(*) FROM Activities;

SELECT 'running select * FROM Users U, Subscriptions S WHERE U.user_id = S.user_id LIMIT 10' AS '';
SELECT * FROM Users U, Subscriptions S WHERE U.user_id = S.user_id LIMIT 10;

SELECT 'running select * from Users U, Activities A where U.user_id = A.user_id LIMTI 10' AS '';
SELECT * FROM Users U, Activities A WHERE U.user_id = A.user_id LIMIT 10;
