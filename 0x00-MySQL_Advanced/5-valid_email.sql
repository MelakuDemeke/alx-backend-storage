-- Define a trigger that sets valid_email to 0 when the email is changed during an update.
DELIMITER $$
CREATE TRIGGER reset_valid_email
BEFORE UPDATE
ON users
FOR EACH ROW
BEGIN
    IF NEW.email != OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END $$
DELIMITER;
