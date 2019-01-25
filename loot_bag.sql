PRAGMA foreign_keys = ON;
DROP TABLE IF EXISTS Toy_Sac;
DROP TABLE IF EXISTS Kids;

CREATE TABLE `Kids` (
    `KidId`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `Name`    TEXT NOT NULL,
    `Gender`    TEXT NOT NULL
);

CREATE TABLE 'Toy_Sac' (
    'ToyId' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'ToyName' TEXT NOT NULL,
    'Delivered' BOOLEAN DEFAULT 0,
    'KidID' INTEGER NOT NULL,
     FOREIGN KEY(`KidId`)
     REFERENCES `Kids`(`KidId`)
)