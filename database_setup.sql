-- creates the database and a user for the project

CREATE DATABASE IF NOT EXISTS finding_mimo_db;
CREATE USER IF NOT EXISTS 'mimo'@'localhost' IDENTIFIED BY 'finding_mimo_2024';
GRANT ALL PRIVILEGES ON `finding_mimo_db`.* TO 'mimo'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'mimo'@'localhost';
FLUSH PRIVILEGES;
