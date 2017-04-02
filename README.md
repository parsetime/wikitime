# wikitime
Progetto WIKI: progetto di alternanza scuola-lavoro
Il progetto, sviluppato da Professori della scuola, intende mettere nelle condizioni gli studenti di lavorare alla creazione o al miglioramento sulle piattaforme wiki di alcuni contenuti legati a discipline varie.

Il sw allegato pfm_xx.py è un piccolo script python che consente di estrarre i dati dai registri elettronici degli studenti al fine di quantizzare il loro impegno sul progetto. Rilasciato su licenza CC-BY.
E' stato provato su piattaforma Linux (XFCE, Mint 14.04) e win7. Funziona da riga di comando.
E' necessario il collegamento ad internet durante il funzionamento.

Istruzioni:
1) scaricare il file pfm_xx.py
2) posizionarlo in una directory vuota
3) in ambiente win scaricare ed installare python 3 (https://www.python.org/downloads/)
4) in ambiente linux python dovrebbe essere già installato. Assicurarsi di avere la versione 3 o superiore.

In ambiente win entrare in modo terminale utilizzando il comando da start "esegui --> cmd", in ambiente linux utilizzare una finestra terminale. Posizionarsi nella directory dove si trova lo script.

Due modi di funzionamento:

modo teacher (opzione -t): genera un file csv con i nomi degli studenti ed il loro impegno totale.
modo student (opzione -s): genera un file csv relativo al singolo studente con i tempi dettagliati per ogni sessione

Linea di comando:

python3 pfm.py -t url_della_pagina_del_progetto

python3 pfm.py -s url_della_pagina_dello_studente/essa

I file generati di tipo csv possono essere letti da un qualsiasi foglio elettronico sia in ambiemte win che in ambiente linux.

In ambiente win per richiamare l'interprete python utilizzare python e non python3. Controllare comunque prima di lanciare lo script il funzionamento dell'interprete python lanciandolo da terminale con python o python3. Quando si è sicuri che l'interprete lavori si può utilizzre lo script.

ATTENZIONE: il programma è sperimentale e dipende dal layout delle pagine web generate dal progetto. Il parser fa del suo meglio ed è stato testato su pagine esistenti, ma non è infallibile. In ogni caso gli errori possono sempre essere presenti anche sul calcolo dei tempi. Controllare ACCURATAMENTE i risultati. Il programma è sempre suscettibile di miglioramenti e non si assumono responsabilità per errori vari. La collaborazione dei professori interessati è la benvenuta ed è indispensabile per dare loro un tool funzionante ed utile.

Per segnalazioni bug o info: parsetime@gmail.com

