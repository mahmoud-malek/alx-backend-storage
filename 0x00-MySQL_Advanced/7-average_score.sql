-- a SQL script that creates a stored procedure
-- ComputeAverageScoreForUser that computes
-- and store the average score for a student. Note: An average score can be a decimal

DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN

	DECLARE total_score INT;
	SELECT SUM(score) INTO total_score
	FROM corrections
	WHERE user_id = user_id;

	DECLARE total_projects INT;
	SELECT COUNT(project_id) INTO total_projects
	FROM corrections
	WHERE user_id = user_id;

	DECLARE average_score DECIMAL(5,2);
	SET average_score = total_score / total_projects;
	
	INSERT INTO users (average_score) VALUES (average_score)
	WHERE id = user_id;

END$$
DELIMITER ;