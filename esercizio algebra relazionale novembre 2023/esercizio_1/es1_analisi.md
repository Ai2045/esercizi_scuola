Esercizio 1
Dato il seguente schema logico:
RIVISTE(CodR, NomeR, Editore)
ARTICOLI(CodA, Titolo, Argomento, CodR)
a. Disegnare il corrispondente modello E/R
b. Risolvere in algebra relazionale le seguenti interrogazioni:
1) Trovare il codice e il nome delle riviste che hanno pubblicato almeno un articolo di argomento 
“motociclismo”
2) Elenco degli articoli pubblicati sulla rivista “Focus” che trattano di “Intelligenza Artificiale”
3) Nome delle riviste che hanno come Editore “Einaudi” e che iniziano con la lettera G
4) Elenco degli editori che non hanno pubblicato articoli sulla “IA”
5) Trovare il nome delle riviste che pubblicano articoli di motociclismo e di automobilismo

π codR, nomeR(riviste ⨝ riviste.codR = articoli.codR(σ argomento = 'motociclismo'))
π codA, titolo((σ nomeR = 'Focus'(riviste)) ⨝ riviste.codR = articoli.codR (σ argomento = 'Intelligenza Artificiale'))
π nomeR (σ editore = 'Einaudi' ∧ nomeR LIKE 'G%')
π editore (riviste ⨝ riviste.codR = articoli.codR (σ argomento ≠ 'IA' (articoli))))
π nomeR (riviste ⨝ riviste.codR = articoli.codR(σ argomento = 'motociclismo' ∧ argomento = 'automobilismo'))


CREATE TABLE riviste(
	codR CHAR(10) PRIMARY KEY,
    nomeR VARCHAR(20) NOT NULL,
    editore VARCHAR(20) NOT NULL
);

CREATE TABLE articoli(
	  codA CHAR(10) PRIMARY KEY,
    codR VARCHAR(10) NOT NULL,
    titolo VARCHAR(20) NOT NULL,
    argomento VARCHAR(50) NOT NULL,
    FOREIGN KEY (codR) REFERENCES riviste(codR)
);


SELECT
	riviste.codR, riviste.nomeR
FROM
	riviste, articoli
WHERE
	argomento = 'motociclismo'
 	AND riviste.codR = articoli.codR


SELECT 
	articoli.CodA, articoli.Titolo
FROM 
	riviste, articoli
WHERE 
	riviste.NomeR = 'Focus'
	AND riviste.CodR = articoli.CodR
	AND argomento = 'Intelligenza Artificiale';


SELECT 
	riviste.NomeR
FROM 
	riviste
WHERE 
	riviste.Editore = 'Einaudi'
	AND riviste.NomeR LIKE 'G%';


SELECT
	DISTINCT riviste.Editore
FROM
	riviste
	LEFT JOIN articoli ON riviste.CodR = articoli.CodR
WHERE 
	articoli.Argomento != 'Intelligenza Artificiale' 
 	OR articoli.Argomento IS NULL;


SELECT
	DISTINCT riviste.NomeR
FROM
	riviste, articoli
WHERE
	riviste.CodR = articoli.CodR
	AND (argomento = 'motociclismo' OR argomento = 'automobilismo');

