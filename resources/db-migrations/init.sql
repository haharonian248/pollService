DROP TABLE IF EXISTS user_question_answer;
DROP TABLE IF EXISTS answer_to_question;
DROP TABLE IF EXISTS question;

CREATE TABLE question (
    q_id int(11) NOT NULL AUTO_INCREMENT,
    q_text VARCHAR(300) NOT NULL,
    PRIMARY KEY (q_id)
);

CREATE TABLE answer_to_question (
    a_id int(11) NOT NULL AUTO_INCREMENT,
    a_text VARCHAR(300) NOT NULL,
    q_id int(11) NOT NULL,
    PRIMARY KEY (a_id),
    FOREIGN KEY (q_id) REFERENCES question (q_id)
);

CREATE TABLE user_question_answer (
    r_id int(11) NOT NULL AUTO_INCREMENT,
    user_id INT(11) NOT NULL,
    q_id int(11) NOT NULL,
    a_id int(11) NOT NULL,
    PRIMARY KEY (r_id),
    FOREIGN KEY (q_id) REFERENCES question(q_id) ON DELETE CASCADE,
    FOREIGN KEY (a_id) REFERENCES answer_to_question(a_id) ON DELETE CASCADE
);

INSERT INTO question (q_text) VALUES
('What is your favorite season?'),
('Which type of music do you prefer?'),
('How often do you travel?'),
('What is your preferred programming language?'),
('Which sport do you enjoy the most?'),
('What is your favorite type of movie?'),
('How do you usually commute?'),
('What is your favorite meal of the day?'),
('Which pet would you rather have?'),
('How do you prefer to spend weekends?');

INSERT INTO answer_to_question (a_text, q_id) VALUES
('Spring', 1), ('Summer', 1), ('Autumn', 1), ('Winter', 1),
('Pop', 2), ('Rock', 2), ('Classical', 2), ('Jazz', 2),
('Rarely', 3), ('Sometimes', 3), ('Often', 3), ('Very Often', 3),
('Python', 4), ('JavaScript', 4), ('Java', 4), ('C#', 4),
('Football', 5), ('Basketball', 5), ('Tennis', 5), ('Swimming', 5),
('Action', 6), ('Comedy', 6), ('Drama', 6), ('Horror', 6),
('Car', 7), ('Bus', 7), ('Bike', 7), ('Walk', 7),
('Breakfast', 8), ('Lunch', 8), ('Dinner', 8), ('Snacks', 8),
('Dog', 9), ('Cat', 9), ('Bird', 9), ('Fish', 9),
('Relaxing at home', 10), ('Going out', 10), ('Traveling', 10), ('Exercising', 10);

INSERT INTO user_question_answer (user_id, q_id, a_id)
VALUES
(1, 1, 2),
(1, 3, 1),
(2, 1, 3),
(3, 2, 1),
(3, 4, 2),
(4, 3, 4),
(5, 5, 2);
