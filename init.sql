CREATE TABLE IF NOT EXISTS tweets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    text VARCHAR(255) NOT NULL,
    positive TINYINT(1) NOT NULL,
    negative TINYINT(1) NOT NULL
);