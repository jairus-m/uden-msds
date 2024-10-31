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

-- Insert data into Users table
INSERT INTO Users (user_id, name, subscription_type, date_created)
VALUES
    (1, 'Jairus Martinez', 'free', '2016-09-13'),
    (2, 'Haley Runyan', 'free', '2023-12-21'),
    (3, 'Lionel Sanders', 'premium', '2011-4-21');

-- Create Subscription table if it does not exist
CREATE TABLE IF NOT EXISTS Subscriptions (
    sub_id INT PRIMARY KEY,
    user_id INT,
    payment_interval VARCHAR(255),
    payment_cost INT,
    status VARCHAR(255),
    end_date DATE NULL,
    purchase_date DATE NULL,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- Insert data into Subscriptions table
INSERT INTO Subscriptions (sub_id, user_id, payment_interval, payment_cost, status, end_date, purchase_date)
VALUES
    (2, 3, 'monthly', 20, 'active', NULL, '2015-01-21');

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

-- Insert data into Activities table for user_id = 1
INSERT INTO Activities (actv_id, user_id, actv_name, actv_type, avg_speed, duration, heartrate, upload_date)
VALUES
    (1, 1, 'Morning Run', 'Running', 8, 45, 150, '2024-01-25'),
    (2, 1, 'Afternoon Cycling', 'Cycling', 20, 60, 120, '2024-01-26'),
    (3, 1, 'Evening Hike', 'Hiking', 5, 120, 110, '2024-01-27'),
    (4, 1, 'Indoor Workout', 'Gym', 10, 30, 130, '2024-01-28'),
    (5, 1, 'Swimming Session', 'Swimming', 2, 60, 140, '2024-01-29');

-- Insert data into Activities table for user_id = 2
INSERT INTO Activities (actv_id, user_id, actv_name, actv_type, avg_speed, duration, heartrate, upload_date)
VALUES
    (6, 2, 'Cycling to Work', 'Cycling', 15, 30, 125, '2024-01-25'),
    (7, 2, 'Yoga Session', 'Yoga', NULL, 45, NULL, '2024-01-26'),
    (8, 2, 'Afternoon Walk', 'Walking', 4, 60, 105, '2024-01-27'),
    (9, 2, 'Basketball Game', 'Sports', 12, 90, 140, '2024-01-28'),
    (10, 2, 'Gym Training', 'Gym', 8, 45, 130, '2024-01-29');

-- Insert data into Activities table for user_id = 3
INSERT INTO Activities (actv_id, user_id, actv_name, actv_type, avg_speed, duration, heartrate, upload_date)
VALUES
    (11, 3, 'Morning Jog', 'Running', 7, 40, 155, '2024-01-25'),
    (12, 3, 'Climbing Adventure', 'Climbing', 3, 180, 100, '2024-01-26'),
    (13, 3, 'Bike Ride in Park', 'Cycling', 18, 60, 120, '2024-01-27'),
    (14, 3, 'Cardio Workout', 'Gym', 9, 30, 135, '2024-01-28'),
    (15, 3, 'Swimming Practice', 'Swimming', 3, 90, 145, '2024-01-29');


SHOW TABLES;

SELECT 'running describe Users' AS '';
DESCRIBE Users;

SELECT 'running describe Subscriptions' AS '';
DESCRIBE Subscriptions;

SELECT 'running describe Activities' AS '';
DESCRIBE Activities;

SELECT 'running select * from Users' AS '';
SELECT * FROM Users;

SELECT 'running select * from Subscriptions' AS '';
SELECT * FROM Subscriptions;

SELECT 'running select * FROM Users U, Subscriptions S WHERE U.user_id = S.user_id' AS '';
SELECT * FROM Users U, Subscriptions S WHERE U.user_id = S.user_id;

SELECT 'running select * from Users U, Activities A where U.user_id = A.user_id' AS '';
SELECT * FROM Users U, Activities A WHERE U.user_id = A.user_id;
