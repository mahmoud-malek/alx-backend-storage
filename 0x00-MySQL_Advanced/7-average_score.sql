-- A SQL script that creates a stored procedure
-- ComputeAverageScoreForUser that computes
-- and stores the average score for a student. Note: An average score can be a decimal.

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser (IN input_user_id INT)
BEGIN
    
    DECLARE total_score INT;
    DECLARE total_projects INT;
    DECLARE average_score DECIMAL(5,2);

    -- Calculate the total score for the user
    SELECT SUM(score) INTO total_score
    FROM corrections
    WHERE user_id = input_user_id;

    -- Calculate the total number of projects for the user
    SELECT COUNT(project_id) INTO total_projects
    FROM corrections
    WHERE user_id = input_user_id;
    
    -- Compute the average score
    SET average_score = CAST(total_score AS DECIMAL(5,2)) / total_projects;
    
    -- Update the user's average score
    UPDATE users
    SET average_score = average_score
    WHERE id = input_user_id;

END$$
DELIMITER ;