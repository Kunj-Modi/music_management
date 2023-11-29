create database Music;
use Music;

create table Singers(
	singer_id int auto_increment primary key,
    singer_name varchar(50)
);

create table Genres(
	genre_id int auto_increment primary key,
    genre_name varchar(20)
);

create table Albums(
	album_id int auto_increment primary key,
    album_name varchar(40),
    album_year datetime,
    singer_id int,
    FOREIGN KEY (singer_id) REFERENCES Singers(singer_id)
);

create table Songs(
	song_id int auto_increment primary key,
    song_name varchar(40),
    song_date datetime,
    album_id int,
    genre_id int,
    FOREIGN KEY (album_id) REFERENCES Albums(album_id),
    FOREIGN KEY (genre_id) REFERENCES Genres(genre_id)
);

select * from Songs;
select * from Albums;
select * from Genres;
select * from Singers;

ALTER TABLE Singers
ADD COLUMN dob DATE,
ADD COLUMN gender ENUM('Male', 'Female');

ALTER TABLE Singers
DROP COLUMN dob;

ALTER TABLE Albums MODIFY COLUMN album_year INT;

insert INTO Genres (genre_name) VALUES ('Hip Hop');
insert INTO Genres (genre_name) VALUES ('Romantin');
insert INTO Genres (genre_name) VALUES ('Pop');
insert INTO Genres (genre_name) VALUES ('Country')