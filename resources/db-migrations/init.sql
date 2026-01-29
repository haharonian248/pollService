DROP TABLE IF EXISTS question;
DROP TABLE IF EXISTS answer_to_question;
DROP TABLE IF EXISTS user_question_answer;

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