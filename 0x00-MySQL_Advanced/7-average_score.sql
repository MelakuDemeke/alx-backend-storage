-- This stored procedure calculates and updates the average score for a user based on their corrections.
-- It takes the user's ID as input and sets the average score in the users table.

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT)
BEGIN
    -- Declare a variable to store the average score
    DECLARE avg_score FLOAT;
    
    -- Calculate the average score for the user
    SET avg_score = (SELECT AVG(score) FROM corrections AS C WHERE C.user_id=user_id);
    
    -- Update the users table with the calculated average score
    UPDATE users SET average_score = avg_score WHERE id=user_id;
    
END
$$
DELIMITER ;
