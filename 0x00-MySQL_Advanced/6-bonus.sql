-- A SQL script that creates
-- a stored procedure AddBonus that adds a new correction for a student.

DELIMITER //
CREATE PROCEDURE AddBonus (IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
    DECLARE project_id INT;

    -- Check if the project exists
    SELECT id INTO project_id
    FROM projects
    WHERE name = project_name;

    -- If the project does not exist
    IF project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (project_name);
        SET project_id = LAST_INSERT_ID();
    END IF;

    -- Insert the score
    INSERT INTO corrections (user_id, project_id, score) 
    VALUES (user_id, project_id, score);

    -- Update the total score
    UPDATE users
    SET average_score = average_score + score
	WHERE id = user_id;
END;
//
DELIMITER ;