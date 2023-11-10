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
