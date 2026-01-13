-- Create database hbtn_0d_2
CREATE DATABASE hbtn_0d_2;
-- Drop if the user user_0d_1 already exists
DROP USER IF EXISTS 'user_0d_1'@'localhost';
-- Create user_0d_2
CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
--  SELECT privilege for user_0d_2
GRANT CREATE SELECT *.* TO 'user_0d_2'@'localhost' WITH GRANT OPTION;
