USE dash;

-- One must involve a two-way or three-way join with a where clause that limits the results to 20 of fewer tuples
-- This is a 3 way join between Users, Subscriptions, and Activities. It filters based on all 3 tables to result in 3 record tuples. 
-- This query finds the oldest premium subscribers who have 99 activites or more and returns the user id, subscription type, and payment interval.
SELECT '1. Return the user_id, subscription_type, and payment_interval of the oldest premium subscribers that pay semi-annually and have more than 99 activities.' AS '';
SELECT DISTINCT U.user_id, U.subscription_type, S.payment_interval, S.purchase_date
FROM Users U
INNER JOIN Subscriptions S 
    ON U.user_id = S.user_id
INNER JOIN Activities A  
    ON U.user_id = A.user_id
WHERE U.subscription_type='premium' AND S.payment_interval ='semi-annual' 
    AND U.user_id IN (
    SELECT user_id
    FROM Activities
    GROUP BY user_id
    HAVING COUNT(*) > 99
    )
ORDER BY S.purchase_date;

-- One must be an aggregate using a group by clause.
-- This is a simple Group By that returns counts of the two subscription types
-- This query gets the counts of both subscription type and includes the amount of revenue for both subscription types.
SELECT '2. Return the count and total revenue of each subscription type and order by count.' AS '';
SELECT U.subscription_type, COUNT(*) AS num_types, SUM(payment_cost) as total_revenue
FROM Users U
LEFT OUTER JOIN Subscriptions S ON U.user_id = S.user_id
GROUP BY U.subscription_type
ORDER BY num_types DESC; 

-- One must be an aggregate using a group by clause and a having clause
-- Group by + Having query that returns user data based on those uploading 10 activities or less for paying, premium accounts. 
-- Inner query returns users who have uploaded less than 10 activities and outer query returns the number of users that have uploaded 1-10 activities. 
SELECT '3. Return the count of premium users that have less than 10 activities uploaded and group by activity count.' AS '';
SELECT activity_count, COUNT(*) as num_users
FROM (
    SELECT U.user_id, COUNT(*) as activity_count
    FROM Users U
    INNER JOIN Activities A ON U.user_id = A.user_id
    WHERE U.subscription_type = 'premium'
    GROUP BY U.user_id
    HAVING COUNT(*) <= 10
    ORDER BY activity_count
) as losers
GROUP BY activity_count;



-- Simple insert
SELECT '4. Insert user10001.' AS '';

SELECT 'Before: RUN SELECT * FROM Users ORDER BY user_id DESC LIMIT 3' AS '';
SELECT * FROM Users ORDER BY user_id DESC LIMIT 3;

-- INSERT command
INSERT INTO Users (user_id, name, subscription_type, date_created)
VALUES (10001, 'user10001', 'free', '2024-02-11');

SELECT 'After: RUN SELECT * FROM Users ORDER BY user_id DESC LIMIT 3' AS '';
SELECT * FROM Users ORDER BY user_id DESC LIMIT 3;

-- Simple update
SELECT '5. Update user10001 to premium.' AS '';

SELECT 'Before: RUN SELECT * FROM Users WHERE user_id = 10001' AS '';
SELECT * FROM Users WHERE user_id = 10001;

-- UPDATE command
UPDATE Users
SET subscription_type = 'premium'
WHERE user_id = 10001;

SELECT 'After: SELECT * FROM Users WHERE user_id = 10001' AS '';
SELECT * FROM Users WHERE user_id = 10001;

-- insert these new users and then update them
INSERT INTO Users (user_id, name, subscription_type, date_created)
VALUES 
    (10002, 'user10002', 'test', '2024-02-12'),
    (10003, 'user10003', 'test', '2024-02-13'),
    (10004, 'user10004', 'test', '2024-02-14');

-- Update several tuples at once
SELECT '6. Update test subscription types date_created column to NULL.' AS '';

SELECT 'Before: RUN SELECT * FROM Users WHERE user_id > 10000' AS '';
SELECT * FROM Users WHERE user_id > 10000;

-- UPDATE command for mulitple records
UPDATE Users
SET date_created = NULL
WHERE subscription_type = 'test';

SELECT 'After: RUN SELECT * FROM Users WHERE user_id > 10000' AS '';
SELECT * FROM Users WHERE user_id > 10000;

-- Delete new users
DELETE FROM Users
WHERE user_id > 10000;