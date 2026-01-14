-- Drop if the user user_0d_1 already exists
DROP USER IF EXISTS 'user_0d_1'@'localhost';
-- Creates the MySQL server user user_0d_1.
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Set to have all privileges on your MySQL server
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' FLUSH PRIVILEGES;
