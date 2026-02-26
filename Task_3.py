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
('Вау мой Абоба', 210, 4),
('my own', 100, 4),
('own my', 100, 4),
('my', 100, 4),
('oh my god', 100, 4),
('myself', 100, 4),
('by myself', 100, 4),
('bemy self', 100, 4),
('myself by', 100, 4),
('by myself by', 100, 4),
('beemy', 100, 4),
('premyne', 100, 4);

INSERT INTO Collection(name, date) VALUES
('Легендарный рок', '2020-01-01'),
('Лучший рэп', '2019-01-01'),
('Романтический плейлист', '2022-01-01'),
('Все стили вместе', '2018-01-01');

INSERT INTO CollectTracks(collection_id, tracks_id) VALUES
(1, 1), (1, 3), (2, 2), (2, 4), (3, 5), (4, 6);


#Начало 2 задания


SELECT name, duration FROM Tracks
ORDER BY duration DESC
LIMIT 1;

SELECT name FROM Tracks
WHERE duration >= 210;

SELECT name FROM Collection
WHERE EXTRACT(YEAR FROM date) BETWEEN 2018 AND 2020;

SELECT name FROM Performers
WHERE name NOT LIKE '% %';

SELECT name FROM Tracks
WHERE name ILIKE 'мой'
OR name ILIKE 'мой  %'
OR name ILIKE '% мой %'
OR name ILIKE '% мой'
OR name ILIKE 'my %'
OR name ILIKE '% my %'
OR name ILIKE '% my'
OR name ILIKE 'my';


#Начало 3 задания


SELECT g.name, COUNT(p.id) FROM Genre g
JOIN PerfGenre pg ON g.id = pg.genre_id
JOIN Performers p ON pg.performers_id = p.id
GROUP BY g.name;

SELECT COUNT(t.id) FROM Tracks t
JOIN Album a ON t.album_id = a.id
WHERE EXTRACT(YEAR FROM a.date) IN (2019, 2020);

SELECT a.name, ROUND(AVG(t.duration)) FROM Tracks t
JOIN Album a ON t.album_id = a.id
GROUP BY a.name;

SELECT p.name FROM Performers p
WHERE p.id NOT IN (
    SELECT DISTINCT performers_id
    FROM AlbPerformers ap
    JOIN Album a ON ap.album_id = a.id
    WHERE EXTRACT(YEAR FROM a.date) = 2020
);

SELECT DISTINCT Collection.name FROM Collection
JOIN CollectTracks ON Collection.id = Collecttracks.сollection_id
JOIN Tracks ON CollectTracks.tracks_id = Tracks.id
JOIN Album ON Tracks.album_id = Album.id
JOIN AlbPerformers ON Album.id = AlbPerformers.album_id
JOIN Performers ON AlbPerformers.performers_id = Performers.id
WHERE Performers.name = 'Король и Шут';