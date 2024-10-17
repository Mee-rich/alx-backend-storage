--A script that create a table users
-- id, name, email, country[US, CO, TN]

CREATE TABLE IF NOT EXIST users (
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255)
	country ENUM('US', 'CO', 'TN) DEFAULT 'US' NOT NULL
);
