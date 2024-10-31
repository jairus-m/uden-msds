-- violates foreign constraint since user 10001 does not exist
SELECT 'inserting non-existing user to Subscriptions table:' AS '';
INSERT INTO Subscriptions (sub_id, user_id, payment_interval, payment_cost, purchase_date, end_date, status)
VALUES (1, 15001, 'Monthly', 10, '2024-02-22', '2024-03-22', 'Active');
