-- Creates the user user_0d_1 with all privileges.
CREATE USER 
    IF NOT EXISTS 'user_0d_1'@'localhost'
    IDENTIFIED By 'user_0d_1_pwd';
GRANT ALL privileges
   ON *.*
   TO 'user_0d_1'@'localhost';