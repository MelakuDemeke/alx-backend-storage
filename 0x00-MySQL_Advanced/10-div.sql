-- This SQL statement creates a function named SafeDiv, which divides two numbers.
-- It returns the result of dividing the first number by the second number unless the second number is equal to 0, in which case it returns 0.

DROP FUNCTION IF EXISTS SafeDiv;
DELIMITER $$
CREATE FUNCTION SafeDiv(dividend INT, divisor INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
    DECLARE result FLOAT;
    IF divisor = 0 THEN
        SET result = 0;
    ELSE
        SET result = dividend / divisor;
    END IF;
    RETURN result;
END
$$ 
DELIMITER ;
