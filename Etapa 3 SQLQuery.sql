CREATE TABLE CompanyProfiles (
		Simbolo VARCHAR (200) NOT NULL,
        Compania VARCHAR(100),
		Sector VARCHAR (200),
		Ubicacion VARCHAR (200),
        Fundada VARCHAR
);

CREATE TABLE Companies (
		Date DATE NOT NULL,
        Precio_cierre FLOAT,
		Ticker VARCHAR(200) NOT NULL,
        
		);


		--Creación llaves primarias
ALTER TABLE CompanyProfiles
ADD CONSTRAINT PK_CompanyProfiles PRIMARY KEY (Simbolo);

ALTER TABLE Companies
ADD CONSTRAINT PK_Companies PRIMARY KEY ("Date", Ticker);

ALTER TABLE Companies
ADD CONSTRAINT FK_CompaniesProfiles
FOREIGN KEY (Ticker) REFERENCES CompanyProfiles(Simbolo);

SELECT * FROM CompanyProfiles;
SELECT * FROM Companies;
ALTER TABLE CompanyProfiles
ALTER COLUMN Fundada VARCHAR(100);

USE Trabfinalf3