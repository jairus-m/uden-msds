-- this procedure takes in a user_id and calulates/returns their total activties, total duration, and total distance traveled
DELIMITER //

DROP PROCEDURE IF EXISTS GetUserActivitySummary;
CREATE PROCEDURE GetUserActivitySummary(IN input_user_id INT)
BEGIN
  -- Declare variables
  DECLARE total_activity_count INT;
  DECLARE total_duration INT;
  DECLARE total_distance INT;

  -- Get total activity count, total duration, and total distance for the user
  SELECT 
    COUNT(*),
    SUM(duration),
    SUM(avg_speed * duration)
  INTO 
    total_activity_count,
    total_duration,
    total_distance
  FROM Activities
  WHERE user_id = input_user_id;

  -- Return total activity count, total duration, and total distance
  SELECT 
    input_user_id AS 'User ID',
    total_activity_count AS 'Total Activity Count',
    total_duration AS 'Total Activity Duration (min)',
    total_distance AS 'Total Distance Traveled (miles)';
END //

DELIMITER ;