USE dash;

-- first query WIHTOUT index
SELECT 'Single Relation without index' as '';
SELECT actv_type, AVG(avg_speed) AS avg_speed, AVG(duration) AS avg_duration, AVG(heartrate) AS avg_heartrate
FROM Activities 
WHERE duration BETWEEN 10 AND 60
GROUP BY actv_type;

-- create temp activities table with index
CREATE TEMPORARY TABLE Activities_Index AS
SELECT *
FROM Activities;

CREATE INDEX idx_temp_activities_duration ON Activities_Index (duration);

-- first query WITH index
SELECT 'Single Relation WITH index on user_id' as '';
SELECT actv_type, AVG(avg_speed) AS avg_speed, AVG(duration) AS avg_duration, AVG(heartrate) AS avg_heartrate
FROM Activities_Index 
WHERE duration BETWEEN 10 AND 60
GROUP BY actv_type;

-- second query WITHOUT index
SELECT 'Two relation join without index' as '';
SELECT actv_type, AVG(avg_speed) AS avg_speed, AVG(duration) AS avg_duration, AVG(heartrate) AS avg_heartrate
FROM Activities A
INNER JOIN Users U ON A.user_id = U.user_id
WHERE A.heartrate BETWEEN 100 AND 120 AND A.duration BETWEEN 10 AND 60
GROUP BY actv_type
HAVING AVG(duration) = 120/2;


-- second query WITH index

SELECT 'Two relation join WITH index' as '';
SELECT actv_type, AVG(avg_speed) AS avg_speed, AVG(duration) AS avg_duration, AVG(heartrate) AS avg_heartrate
FROM Activities_Index A
INNER JOIN Users U ON A.user_id = U.user_id
WHERE A.heartrate BETWEEN 100 AND 120 AND A.duration BETWEEN 10 AND 60
GROUP BY actv_type
HAVING AVG(duration) = 120/2;