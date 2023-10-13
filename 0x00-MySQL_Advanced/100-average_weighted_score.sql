-- This stored procedure, 'ComputeAverageWeightedScoreForUser', calculates and stores the average weighted score for a student.
-- It takes a user's ID as input and computes the weighted average of scores based on the associated projects.

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
    IN user_id INT
)
BEGIN
    -- Declare a variable to store the weighted average score
    DECLARE weighted_avg_score FLOAT;
    
    -- Calculate the weighted average score
    SET weighted_avg_score = (
        SELECT SUM(C.score * P.weight) / SUM(P.weight) 
        FROM users AS U 
        JOIN corrections AS C ON U.id = C.user_id 
        JOIN projects AS P ON C.project_id = P.id 
        WHERE U.id = user_id
    );
    
    -- Update the 'average_score' for the user
    UPDATE users SET average_score = weighted_avg_score WHERE id = user_id;
END
$$
DELIMITER ;
