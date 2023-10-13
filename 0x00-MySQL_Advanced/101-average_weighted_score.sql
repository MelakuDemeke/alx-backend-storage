-- This stored procedure, 'ComputeAverageWeightedScoreForUsers', calculates and stores the average weighted scores for all students.
-- It computes the weighted average score for each student based on associated projects and updates their 'average_score' in the users table.

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    -- Update the 'average_score' for all users with their weighted average scores
    UPDATE users AS U, 
    (
        SELECT U.id, SUM(C.score * P.weight) / SUM(P.weight) AS w_avg 
        FROM users AS U 
        JOIN corrections AS C ON U.id = C.user_id 
        JOIN projects AS P ON C.project_id = P.id 
        GROUP BY U.id
    )
    AS WA
    SET U.average_score = WA.w_avg 
    WHERE U.id = WA.id;
END
$$
DELIMITER ;
