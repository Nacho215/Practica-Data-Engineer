USE master;
DROP DATABASE unidad13;
GO
CREATE DATABASE unidad13;
GO
USE unidad13;
GO
CREATE TABLE Alumno(
	legajo INT PRIMARY KEY,
	nombre VARCHAR(45) NOT NULL,
	apellido VARCHAR(45) NOT NULL,
	fecha_nacimiento DATE
);

CREATE TABLE Materia(
	codigo INT PRIMARY KEY,
	descripcion VARCHAR(200)
);

CREATE TABLE Cursa(
	legajo INT FOREIGN KEY REFERENCES Alumno(legajo),
	codigo INT FOREIGN KEY REFERENCES Materia(codigo)
);

INSERT INTO Alumno VALUES
(4233, 'Pedro', 'Álvarez', '1995-08-15'),
(3235, 'Juan Ignacio', 'Hernández', '1997-05-21'),
(4563, 'Martín', 'Ledesma', '1996-04-03'),
(4421, 'Camila', 'Morales', '1999-11-24'),
(3784, 'Belén', 'Tapia', '1995-01-09');

INSERT INTO Materia VALUES
(1, 'Matemáticas'),
(2, 'Física'),
(3, 'Química'),
(4, 'Programación'),
(5, 'Psicología');

INSERT INTO Cursa VALUES
(3784, 1),
(3235, 4),
(4563, 3),
(4563, 5),
(3784, 2);