Esercizio3
Dato il seguente schema logico:
SPETTACOLI(CodS, Titolo, Compagnia, Durata)
CARTELLONI(Data, OraInizio, NomeTeatro, CodS)
a. Disegnare il corrispondente modello E/R
b. Risolvere in algebra relazionale le seguenti interrogazioni:
1) Trovare il nome delle compagnie che hanno tenuto spettacoli il 2/11/2023 ma non il 3/11/2023
2) Trovare i titoli degli spettacoli tenuti dalla compagnia “Bolle and friends”
3) Trovare i titoli degli spettacoli tenuti al teatro “Grande” che siano durati più di 120 minuti
4) Trovare il nome delle compagnie che si sono esibite ad ottobre 2023 al teatro “Grande”
5) Stampare il calendario del teatro “Arcimboldi” per il prossimo mese di dicembre
6) Stampare il nome dei teatri nei quali è stato messo in scena lo spettacolo “il lago dei cigni”

osservazione: non conviene tenere separato data e oraInizio
              meglio CARTELLONI(data, nomeTeatro, codS)
π compagnia (spettacoli ⨝ spettacoli.codS = cartelloni.codS (σ data = '02-11-2023' ∧ data ≠ '03-11-2023'(cartelloni)))
π titolo (σ compagnia = 'Bolle and friends' )
π titolo ((σ durata > 120 (spettacoli)) ⨝ spettacoli.codS = cartelloni.codS (σ nomeTeatro = 'Grande' (cartelloni)))
π compagnia (spettacoli ⨝ spettacoli.codS = cartelloni.codS(σ nomeTeatro = 'Grande' ∧ data ≥ '01-10-2023' ∧ data ≤ '31-10-2023' (cartelloni))))
π titolo, compagnia, durata, data, oraInizio (spettacoli ⨝ spettacoli.codS = cartelloni.codS(σ nomeTeatro = 'Arcimboldi' ∧ data ≥ '01-12-2023' ∧ data ≤ '31-12-2023' (cartelloni))))
π nomeTeatro ((σ titolo = 'il lago dei cigni' (spettacoli)) ⨝ spettacoli.codS = cartelloni.codS (cartelloni))

CREATE TABLE spettacoli(
	  codS CHAR(10) PRIMARY KEY,
    titolo VARCHAR(20) NOT NULL,
    compagnia VARCHAR(30) NOT NULL,
    durata TIME NOT NULL
);

CREATE TABLE cartelloni(
	  data DATETIME PRIMARY KEY,
    codS CHAR(10) NOT NULL,
    nomeTeatro VARCHAR(20) NOT NULL,
    FOREIGN KEY(cods) REFERENCES spettacoli(codS)
);


SELECT 
	DISTINCT compagnia
FROM 
	cartelloni
	JOIN spettacoli ON cartelloni.codS = spettacoli.codS
WHERE
	data = '2023-11-02' 
 	AND data != '2023-11-03';


SELECT 
	titolo
FROM 
	spettacoli
WHERE
	compagnia = 'Bolle and friends';


SELECT 
	titolo
FROM 
	spettacoli
	JOIN cartelloni ON spettacoli.codS = cartelloni.codS
WHERE 
	nomeTeatro = 'Grande' 
 	AND durata > '02:00:00';


SELECT 
	DISTINCT compagnia
FROM 
	spettacoli
	JOIN cartelloni ON spettacoli.codS = cartelloni.codS
WHERE
	nomeTeatro = 'Grande' 
 	AND data BETWEEN '2023-10-01' 
  	AND '2023-10-31';


SELECT 
	titolo, compagnia, durata, data, oraInizio
FROM 
	spettacoli
	JOIN cartelloni ON spettacoli.codS = cartelloni.codS
WHERE 
	nomeTeatro = 'Arcimboldi' 
 	AND data BETWEEN '2023-12-01' 
  	AND '2023-12-31';


SELECT 
	DISTINCT nomeTeatro
FROM 
	cartelloni
	JOIN spettacoli ON cartelloni.codS = spettacoli.codS
WHERE 
	titolo = 'Il lago dei cigni';


