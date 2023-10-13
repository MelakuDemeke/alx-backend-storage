-- This SQL statement creates a view named 'need_meeting' that lists all students with a score below 80 (strict).
-- It also filters out students who either have no 'last_meeting' record or whose last meeting was more than 1 month ago.

DROP VIEW IF EXISTS need_meeting;
CREATE VIEW need_meeting AS 
SELECT name FROM students 
WHERE 
    score < 80 AND 
    (last_meeting IS NULL 
        OR 
    last_meeting < DATE_SUB(CURDATE(), INTERVAL 1 MONTH));
