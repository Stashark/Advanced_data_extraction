CREATE TABLE IF NOT EXISTS Genre (
id SERIAL PRIMARY KEY,
name VARCHAR(40) NOT NULL
);

CREATE TABLE IF NOT EXISTS Performers (
id SERIAL PRIMARY KEY,
name VARCHAR(80) NOT NULL
);

CREATE TABLE IF NOT EXISTS PerfGenre (
id SERIAL PRIMARY KEY,
performers_id INTEGER NOT NULL REFERENCES Performers(id),
genre_id INTEGER NOT NULL REFERENCES Genre(id)
);

CREATE TABLE IF NOT EXISTS Album (
id SERIAL PRIMARY KEY,
name VARCHAR(80) NOT NULL,
date DATE
);

CREATE TABLE IF NOT EXISTS AlbPerformers (
id SERIAL PRIMARY KEY,
performers_id INTEGER NOT NULL REFERENCES Performers(id),
album_id INTEGER NOT NULL REFERENCES Album(id)
);

CREATE TABLE IF NOT EXISTS Tracks (
id SERIAL PRIMARY KEY,
name VARCHAR(40) NOT NULL,
duration INTEGER NOT NULL,
album_id INTEGER NOT NULL REFERENCES Album(id)
);

CREATE TABLE IF NOT EXISTS Collection (
id SERIAL PRIMARY KEY,
name VARCHAR(80) NOT NULL,
date DATE
);

CREATE TABLE IF NOT EXISTS CollectTracks (
id SERIAL PRIMARY KEY,
collection_id INTEGER NOT NULL REFERENCES Collection(id),
tracks_id INTEGER NOT NULL REFERENCES Tracks(id)
);


#Начало 1 задания


INSERT INTO Genre(name) VALUES ('Рок'), ('Рэп'), ('Поп');

INSERT INTO Performers(name) VALUES
('Король и Шут'),
('Noize MC'),
('Егор Крид'),
('Монеточка'),
('Абоба');

INSERT INTO Album(name, date) VALUES
('Камнем по голове', '2001-01-01'),
('Hard Reza', '2020-01-01'),
('Что их держит', '2019-01-01'),
('Незабываемый', '2018-01-01');

INSERT INTO PerfGenre(performers_id, genre_id) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 3),
(5, 1);

INSERT INTO AlbPerformers(performers_id, album_id) VALUES
(1, 1),
(2, 2),
(3, 3),
(5, 4);

INSERT INTO Tracks(name, duration, album_id) VALUES
('Прыгну со скалы', 181, 1),
('На Марсе классно', 260, 2),
('Кукла колдуна', 195, 1),
('За закрытой дверью', 250, 2),
('Будильник', 195, 3),
('Незабудки', 152, 3),
('Каждый раз', 197, 3),
('Мой рок-н-ролл', 197, 3),
('Вау мой Абоба', 210, 4);

INSERT INTO Collection(name, date) VALUES
('Легендарный рок', '2020-01-01'),
('Лучший рэп', '2019-01-01'),
('Романтический плейлист', '2022-01-01'),
('Все стили вместе', '2018-01-01');

INSERT INTO CollectTracks(collection_id, tracks_id) VALUES
(1, 1), (1, 3), (2, 2), (2, 4), (3, 5), (4, 6);


#Начало 2 задания


SELECT name AS название_трека, duration AS продолжительность
FROM Tracks
ORDER BY duration DESC
LIMIT 1;

SELECT name AS название_трека
FROM Tracks
WHERE duration >= 210;

SELECT name AS название_сборника
FROM Collection
WHERE EXTRACT(YEAR FROM date) BETWEEN 2018 AND 2020;

SELECT name AS исполнитель
FROM Performers
WHERE name NOT LIKE '% %';

SELECT name AS название_трека
FROM Tracks
WHERE LOWER(name) LIKE '%мой%' OR LOWER(name) LIKE '%my%';
