--  a SQL script that creates a trigger that resets
-- the attribute valid_email only when the email has been changed.

DROP TRIGGER IF EXISTS reset_email;
CREATE TRIGGER reset_email;

BEFORE UPDATE ON users
UPDATE users
FOR EACH ROW
SET valid_email = 0;
