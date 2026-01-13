-- Create database hbtn_0d_2
CREATE DATABASE hbtn_0d_2;
-- Create user_0d_2
CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
--  SELECT privilege for user_0d_2
GRANT CREATE SELECT *.* TO 'user_0d_2'@'localhost' WITH GRANT OPTION;
