-- a SQL script that creates a stored procedure
-- ComputeAverageScoreForUser that computes
-- and store the average score for a student. Note: An average score can be a decimal

DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
	
	DECLARE total_score INT;
	DECLARE total_projects INT;
	DECLARE average_score DECIMAL(5,2);

	SELECT SUM(score) INTO total_score
	FROM corrections
	WHERE user_id = user_id;


	SELECT COUNT(project_id) INTO total_projects
	FROM corrections
	WHERE user_id = user_id;
	
	SET average_score = total_score / total_projects;
	
	UPDATE users
    SET average_score = average_score
    WHERE id = user_id;

END$$
DELIMITER ;