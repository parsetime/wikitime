## wikitime
Progetto WIKI "Alternanza Nitti": progetto di alternanza scuola-lavoro
Il progetto, sviluppato da Professori dell'Istituto di Istruzione Superiore "F.S. Nitti" di Potenza in collaborazione con Wikimedia Italia, intende mettere nelle condizioni gli studenti di lavorare alla creazione o al miglioramento sulle piattaforme wiki di alcuni contenuti legati a discipline varie.

### descrizione
Il sw allegato pfm_xx.py è un piccolo script python che consente di estrarre i dati dai registri elettronici degli studenti al fine di quantizzare il loro impegno sul progetto. Rilasciato su licenza CC-BY.
E' stato provato su piattaforma Linux (XFCE, Mint 14.04) e win7. Funziona da riga di comando.
E' necessario il collegamento ad internet durante il funzionamento.

E' stato provato sulla pagina progetto dell'Istituto "F.S. Nitti" di Potenza:

[Progetto - Alternanza Scuole - Nitti](https://it.wikipedia.org/wiki/Progetto:Coordinamento/Scuole/Alternanza_Nitti)

Si ringraziano Luigi Catalani, i professori dell'Istituto e tutti gli studenti che partecipano al progetto per la preziosa collaborazione data e Claudio Forziati per l'idea del progetto ed il supporto fornito durante lo sviluppo. E' stato molto stimolante ed un privilegio lavorare con tutti loro.
Grazie.

### come funziona

1) scaricare il file pfm_xx.py
2) posizionarlo in una directory vuota
3) in ambiente win scaricare ed installare python 3 (https://www.python.org/downloads/)
4) in ambiente linux python dovrebbe essere già installato. Assicurarsi di avere la versione 3 o superiore.

In ambiente win entrare in modo terminale utilizzando il comando da start "esegui --> cmd", in ambiente linux utilizzare una finestra terminale. Posizionarsi nella directory dove si trova lo script.

Due modi di funzionamento:

- modo teacher (opzione -t): genera un file csv con i nomi degli studenti ed il loro impegno totale.

- modo student (opzione -s): genera un file csv relativo al singolo studente con i tempi dettagliati per ogni sessione

Linea di comando:

python3 pfm_xx.py -t url_della_pagina_del_progetto

python3 pfm_xx.py -s url_della_pagina_dello_studente/essa

I file generati di tipo csv possono essere letti da un qualsiasi foglio elettronico sia in ambiente win che in ambiente linux.

#### licenza
CC-BY

#### note

In ambiente win per richiamare l'interprete python utilizzare 'python' e non 'python3'. Controllare comunque prima di lanciare lo script il funzionamento dell'interprete python richiamandolo da terminale con 'python' o 'python3'. Quando si è sicuri che l'interprete lavori si può utilizzare lo script. 
Durante il processo di parsing, in modo '-t', per le pagine su cui il parsing ha trovato difficoltà ad estrarre i dati, vengono indicate le pagine di errore. Si può effettuare quindi un controllo visivo per correggere gli eventuali errori di digitazione dei tempi e ripetere il processo.

#### ATTENZIONE: 

il programma è sperimentale e dipende dal layout delle pagine web generate dal progetto. E' stato scritto in poco tempo ed in qualche notte insonne. Il parser fa del suo meglio ed è stato testato su pagine esistenti, ma non è infallibile. In ogni caso gli errori possono sempre essere presenti anche sul calcolo dei tempi. Controllare ACCURATAMENTE i risultati. Il programma è sempre suscettibile di miglioramenti e non si assumono responsabilità per errori vari. La collaborazione dei professori interessati e degli studenti è la benvenuta ed è indispensabile per dare loro un tool funzionante ed utile.


Angelo, IK8VRQ.

Per segnalazioni bug o info: parsetime@gmail.com

'keep learning, keep going!' listen during a #maptime meeting 


