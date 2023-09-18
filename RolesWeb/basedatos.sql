
CREATE DATABASE Estudiantes;

USE Estudiantes;


CREATE TABLE Estudiante (
    id SERIAL PRIMARY KEY,
    programa VARCHAR(255) NOT NULL,
    codigo VARCHAR(255) NOT NULL,
    email_institucional VARCHAR(255) NOT NULL,
    email_personal VARCHAR(255) NOT NULL,
    telefono VARCHAR(255) NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    periodo_lectivo VARCHAR(255) NOT NULL
);

