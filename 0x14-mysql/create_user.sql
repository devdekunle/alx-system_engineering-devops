-- create a user holberton_user
CREATE USER IF NOT EXISTS 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT ALL PRIVILEGES ON *.* TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;
