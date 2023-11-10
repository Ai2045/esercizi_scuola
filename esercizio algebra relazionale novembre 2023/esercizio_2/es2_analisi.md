Esercizio 2
Dato il seguente schema logico:
VELISTI(vID, vNome, Esperienza, DataNascita)
BARCHE(bID, bNome, Colore)
PRENOTAZIONI(vID, bID, Data)
a. Disegnare il corrispondente modello E/R
b. Risolvere in algebra relazionale le seguenti interrogazioni:
1) Trovare i nomi dei velisti che hanno prenotato almeno una barca rossa oppure una barca verde
2) Trovare il nome delle barche prenotate nel mese di novembre 2023
3) Trovare i velisti minorenni con livello di esperienza “base”
4) Il nome dei velisti che hanno prenotato una barca gialla nel mese di aprile 2023
5) Il nome delle barche guidate da velisti con esperienza “senior”
6) Trovare il codice dei velisti che non hanno mai prenotato barche rosse

π vNome ((σ colore = 'rosso' ∨ colore = 'verde'(barche)) ⨝ barche.bID = prenotazioni.bID(velisti ⨝ velisti.vID = prenotazioni.vID (prenotazioni)))

π bNome (barche ⨝  barche.bID = prenotazioni.bID (σ data ≥ '01-04-2023' AND data ≤ '30-04-2023' (prenotazioni)))

π vID, vNome, esperienza, dataNascita(σ (CURRENT_DATE - dataNascita > 18*356) AND esperienza = 'base')

π vNome ((σ colore = 'giallo' (barche)) ⨝ barche.bID = prenotazioni.bID(velisti ⨝ velisti.vID = prenotazioni.vID (σ data ≥ '01-04-2023' AND data ≤ '30-04-2023' (prenotazioni)))

π bNome ((barche ⨝ barche.bID = prenozioni.bID (prenotazioni))⨝ velisti.vID = prenozioni.vID (σ esperienza = 'senior'	(velisti)))

π vID ((velisti ⨝ velisti.vID = prenotazioni.vID (prenotazioni))⨝ barche.bID = prenozioni.bID (σ colore ≠ 'rosso' (barche)))

CREATE TABLE barche(
	  bID INT PRIMARY KEY AUTO_INCREMENT,
    bNome VARCHAR(20) NOT NULL,
    colore VARCHAR(10) NOT NULL
);

CREATE TABLE velisti(
	  vID INT PRIMARY KEY AUTO_INCREMENT,
    vNome VARCHAR(50) NOT NULL,
    esperienza VARCHAR(15) NOT NULL,
    dataNascita DATE NOT NULL
);

CREATE TABLE prenotazioni(
	  vID INT NOT NULL,
    bID INT NOT NULL,
    data DATETIME NOT NULL,
    FOREIGN KEY (vID) REFERENCES velisti(vID),
    FOREIGN KEY (bID) REFERENCES barche(bID)
);

SELECT 
	DISTINCT v.vNome
FROM
	VELISTI v, BARCHE b, PRENOTAZIONI p
WHERE
	b.colore IN ('rosso', 'verde')
	AND b.bID = p.bID
	AND p.vID = v.vID;

