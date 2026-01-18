
CREATE TABLE code
(
    selected_sentence INTEGER NOT NULL,
    start_char INTEGER NOT NULL,
    lenght INTEGER NOT NULL
);

INSERT INTO code (selected_sentence, start_char, lenght)
VALUES
(14, 98, 4),
(114, 3, 5),
(618, 72, 9),
(630, 7, 3),
(932, 12, 5),
(2230, 50, 7),
(2346, 44, 10),
(3041, 14, 5)
;

CREATE VIEW message AS
SELECT substr(
    sentences.sentence,
    code.start_char,
    code.lenght
) AS 'phrase'
FROM
code JOIN sentences ON code.selected_sentence = sentences.id;

