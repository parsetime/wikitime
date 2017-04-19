#!/usr/bin/python3


import re
import urllib.request as ur
import time
import datetime
import sys
import csv
import os

def goodevening():
	print()
	print ("Fine elaborazione. Il file: risultati_totali.csv è stato creato")
	print ("Il file è importabile come foglio elettronico")
	print ()
	print ("pfm_03: versione del 01.04.2017")
	print ("per contatti, bug o info: parsetime@gmail.com")
	print ("Rilasciato con licenza: CC-BY")
	print ()


def goodmorning():
	print ()
	print ("pfm_02: versione del 01.04.2017")
	print ("per contatti, bug o info: parsetime@gmail.com")
	print ("Rilasciato con licenza: CC-BY")
	print ()
	 
def myhelp():
	print ()
	print ("Uso del programma:")
	print("-----------------------------------------------------------")
	print ("python3 pfm_xx.py -t teacherpageurl")
	print ("oppure:")
	print ("python3 pfm_xx.py -s studentpageurl")
	print("-----------------------------------------------------------")
	print ()

arg=sys.argv

goodmorning()


if  len(arg) < 3:
	print
	print ("Troppi pochi parametri")
	print
	myhelp()
	exit()

mymode="unset"

if arg[1]=="-t" or arg[1]=="-tv":
	print ("Parametro in  modo insegnante: genera un file riassuntivo degli studenti")
	mymode ="-t"
	if arg[1]=="-tv":
		myverb="ON"
	else:
		myverb="OFF"
if arg[1]=="-s" or arg[1]=="-sv":
	print ("Parametro in modo studente: genera un file relativo agli impegni del singolo studente")
	mymode="-s"
	if arg[1]=="-sv":
		myverb="ON"
	else:
		myverb="OFF"
if mymode=="unset":
	print ("Parametro: "+ str(arg[1]) + " non valido")
	myhelp()
	exit()

myparurl=arg[2]

kt=myparurl.find('Progetto:')
ks=myparurl.find('Utente:')

if kt >0:
	# siamo in teacher mode
	# teacherpage_url='https://it.wikipedia.org/wiki/Progetto:Coordinamento/Scuole/Alternanza_Nitti'
	teacherpage=arg[2]
	print ("Teacher mode ON")
	print
	
if ks >0:
	# siamo in student mode
	#pageurl='https://it.wikipedia.org/wiki/Utente:Uomovariabile/Aula/test2'
	pageurl=arg[2]
	print ("Student mode ON")
	print

if  ((kt<0) and (mymode=="-t")):
	print ("L'indirizzo della pagina non sembra essere corretto per il modo insegnante")
	exit()

if  ((ks<0) and (mymode=="-s")):
	print ("L'indirizzo della pagina non sembra essere corretto per il modo studente")
	exit()


# modelli di ricerca per il parsing  #
# ---------------------------------------------------------------------
text1 = '<p><b>Sessione \d+</b></p>'
text2 = '<li>inizio sessione:'
text3 = '<li>fine sessione:'
text4 = '<li>attività svolta:'
text5 ='Utente:'

tModel='\d\d:\d\d'
#dModel='\d\d \w\w\w \d\d\d\d'
dModel='.\d \w\w\w \d\d\d\d'
pModel='title="Modifica la sezione Elenco degli studenti partecipanti"'
aModel='<li>--<a href="/w'
uModel='registro elettronico'
rModel='title="Modifica la sezione Gruppi di lavoro e voci"'
# ---------------------------------------------------------------------

totali = datetime.datetime.strptime("00:00:00", "%H:%M:%S")

if mymode=="-t":
	# ---- Scarica la pagina teacher da esaminare su disco ----
	fpage=open ('teacher.txt','wb')
	filepage = ur.urlopen (teacherpage)
	sl = filepage.read()
	fpage.write(sl)
	fpage.close
# -------------------------------------------------

	# Effettua il parsing per estrarre la lista alunni
	# Apre il file del professore in read mode
	f = open( 'teacher.txt' , 'r', encoding="utf8")
	# Apre il file alunni.csv in write mode
	fo = open('alunni.csv', 'w', encoding="utf8")


	i=0
	j=0
	sw=0
	
	# legge riga x riga la pagina del file del progetto facendo il parsing per estrarre la lista alunni 
	for line in f.readlines() :
		myline=line
		#print (i, myline.find(pModel))
		if (myline.find(pModel)>=0):
			sw=1
			# siamo ora nella sezione studenti della pagina
			
		# Questo if viene eseguito per estratte la lista degli sudenti	
		if (sw==1) and (myline.find(aModel)==0):
			k=myline.find('msg')
			ks=myline.find('Utente:',k)
			kq=myline.find('" title',ks)
			kr=myline.find('/',ks)
					
			myUserlink=myline[ks:kq]
			myUserlink='https://it.wikipedia.org/wiki/' + myUserlink
		
			myUsername=myline[ks+7:kr]
			myUsername=myUsername.replace('_', ' ')
			if myverb=="ON":
				print (myUserlink, myUsername)
			else:
				print (".", end ="")
			#salva il record nel file alunni
			fo.write(myUsername + ";" + myUserlink+"\n") 
			j=j+1
			
		i=i+1
	# Chiude il file del professore e quello degli alunni
	
	f.close
	fo.close
	print()
	print ("Pagina progetto scaricata ed analizzata: creato il file csv degli studenti")
	print ("Studenti totali: ", j-1)
	print ()
	
	# resetta la pagina dei totali per prepararsi nel loop a scriverla
	#apre la pagina dei risultati totali
	fo=open('risultati_totali.csv','w') 
	fo.close
	

	
	# legge ora il file csv degli alunni per scaricare pagina x pagina quella di ogni alunno #
	# questo viene fatto solo nel modo teacher per generare i risultati totali per ogni alunno #
	
	# apre il file degli alunni per leggere il link alla pagina dell'alunno#
	filecsv=open("alunni.csv", "rt")
	lettore=csv.reader(filecsv, delimiter=";")

	for riga in lettore:
		if len(riga)>0:
			studente=riga[0] 			# legge il nome dello studente
			link=riga[1]				# legge il link 
			if myverb=="ON":
				print (studente, link)
				print ("Scarica la pagina dello studente")
			# ---- Salva ora la pagina dello studente da esaminare sul disco ----
			try :
				fpage=open (studente + ".txt",'wb')
				filepage = ur.urlopen (link)
				sl = filepage.read()
				fpage.write(sl)
				fpage.close
			except:
				pass
			# -------------------------------------------------
			if myverb=="ON":
				print("Download pagina alunno effettuato")
		
			# Siamo in modo teacher e dobbiamo salvare solo i risultati totali per alunno
			# Apriamo la pagina dello studente appena salvata sul disco e ne facciamo il parsing 
			# calcoliamo la durata totale di tutte le attività
			
			if myverb=="ON":
				print ("Apre la pagina dello studente: ",studente)
				
				
			try:
			
				fpage=open (studente + ".txt",'r', encoding="utf8")	#leggiamo la pagina studente
			
				totali = datetime.datetime.strptime("00:00:00", "%H:%M:%S")
				durata = datetime.datetime.strptime("00:00:00", "%H:%M:%S")
				applicazione=""
			
				#fo.write("Sessione,Data Start,Ora Start, Data End, Ora End, Durata, Argomento\n")
 
				#facciamo il parsing della pagina dello studente
			
				i=0
				for line in fpage.readlines() :
					myline=line
				
					if myverb=="ON":
						print("Test linea:",i)
						
					# estraiamo il numero della sessione
					if re.search(text1, myline) :
						num = re.sub(r'\D', "", myline)
						if myverb=="ON":    
							print ("Numero sessione:",num)
							
						#fo.write(num + ",")
		
					# estraiamo l'inizio dell'attività
					if re.search(text2, myline) :
						if myverb=="ON":
							print  (myline)
		
						if re.search(tModel,myline) :
							myTime=re.search(tModel,myline)
							myTimeStart=myTime.group()
			
						if re.search(tModel,myline) :
							myDate=re.search(dModel,myline)
							myDateStart=myDate.group()
							stringaTempo=myTimeStart + " " + myDateStart
	
							datetimeStart = datetime.datetime.strptime(stringaTempo, "%H:%M %d %b %Y")
							#print("Start: ", datetimeStart)
			
					#fo.write(myDateStart + ",")
					#fo.write(myTimeStart + ",")
			
					# estraiamo la fine dell'attività
					if re.search(text3, myline) :
						if myverb=="ON":
							print  (myline)
		
						if re.search(tModel,myline) :
							myTime=re.search(tModel,myline)  
							myTimeEnd=myTime.group()
						
						if re.search(tModel,myline) :
							myDate=re.search(dModel,myline)  
							myDateEnd=myDate.group()		
							stringaTempo=myTimeEnd + " " + myDateEnd
							datetimeEnd = datetime.datetime.strptime(stringaTempo, "%H:%M %d %b %Y")
						
						#fo.write(myDateEnd + ",")
						#fo.write(myTimeEnd + ",")
			
							durata=datetimeEnd-datetimeStart			# calcola la durata della sessione n
							totali=totali+durata						# somma le durate delle sessioni
					
						mydurata=str(durata)
			
						if (len(mydurata)<8) :
							mydurata="0"+mydurata
						#fo.write(str(mydurata) + ",")
						if myverb=="ON":
							print("Durata sessione: ", num, " -> ", durata)
							print("Totali: ",totali)
						durata = datetime.datetime.strptime("00:00:00", "%H:%M:%S")
				
					# fa il parsing per leggere l'attività svolta		
					if re.search(text4, myline) :
						if myverb=="ON":
							print  (myline)
						p=myline.find(":",0)
						q=myline.find("</li>",0)
						myJob=myline[p+2:q]
						if myverb=="ON":
							print (myJob)
						#fo.write(myJob+ "\n")
		
					# passiamo alla prossima linea del file	
					i=i+1
		
		
				applicazione=str(totali)
				applicazione =applicazione[-8:]
				if myverb=="ON":
					print(applicazione)
	
				# scrive il record dello studente sul file dei totali
				fo=open('risultati_totali.csv','a') #apre la pagina in append dei risultati totali per inserire la riga dello studente
				fo.write(studente + ";" + str(applicazione) + ",\n")
				fo.close							# chiude momentaneamente il file dei totali
			
				fpage.close()						# chiude la pagina dello studente
				print ("Analizzata pagina sudente: ", studente)
				os.remove(studente + ".txt")
			except:
				pass
				
			
			#fo.write(" , , , ,Totali: ," + applicazione +"\n" )
	
	
			# e passa ora al prossimo studente
	

	filecsv.close() # not indented, this happens after the loop

goodevening()




if mymode=="-s":
	vq=myparurl.find(text5)
	vr=myparurl.find("/",vq)
	student_name=myparurl[vq+7:vr]
	
	# resetta la pagina dei totali per prepararsi nel loop a scriverla
	# apre la pagina dei risultati totali
	fo=open(student_name +'.csv','w') 
	fo.close
	
	print ("Scarica la pagina dello studente: " + student_name)
	# -------------------------------------------------
	# Download e salvataggio della pagina dello studente da esaminare sul disco 
	fpage=open (student_name + ".txt",'wb')
	filepage = ur.urlopen (pageurl)
	sl = filepage.read()
	fpage.write(sl)
	fpage.close
	# -------------------------------------------------
	print ("Analisi pagina dello studente: " + student_name)
	fo=open (student_name + ".csv",'w')	#scriviamo la pagina risultati studente
	fo.write ("Sessione;Data inizio; Ora inizio; Data Fine; Ora Fine; Tempo dedicato; Attività svolta \n")
	fpage=open (student_name + ".txt",'r', encoding="utf8")	#leggiamo la pagina studente
	i=0
	for line in fpage.readlines() :
		myline=line
	
		if myverb=="ON":
			print("Test linea:",i)
				
		# estraiamo il numero della sessione
		if re.search(text1, myline) :
			num = re.sub(r'\D', "", myline)
			if myverb=="ON":    
				print ("Numero sessione:",num)
					
			fo.write(num + ";")
		
		# estraiamo l'inizio dell'attività
		if re.search(text2, myline) :
		
			if re.search(tModel,myline) :
				myTime=re.search(tModel,myline)
				myTimeStart=myTime.group()
			
			if re.search(tModel,myline) :
				myDate=re.search(dModel,myline)
				myDateStart=myDate.group()
				stringaTempo=myTimeStart + " " + myDateStart
	
				datetimeStart = datetime.datetime.strptime(stringaTempo, "%H:%M %d %b %Y")
				#print("Start: ", datetimeStart)
			
				fo.write(myDateStart + ";")
				fo.write(myTimeStart + ";")
			
		# estraiamo la fine dell'attività
		if re.search(text3, myline) :
		
			if re.search(tModel,myline) :
				myTime=re.search(tModel,myline)  
				myTimeEnd=myTime.group()
						
			if re.search(tModel,myline) :
				myDate=re.search(dModel,myline)  
				myDateEnd=myDate.group()		
				stringaTempo=myTimeEnd + " " + myDateEnd
				datetimeEnd = datetime.datetime.strptime(stringaTempo, "%H:%M %d %b %Y")
						
				fo.write(myDateEnd + ";")
				fo.write(myTimeEnd + ";")
			
				durata=datetimeEnd-datetimeStart			# calcola la durata della sessione n
				totali=totali+durata						# somma le durate delle sessioni
					
				mydurata=str(durata)
			
				if (len(mydurata)<8) :
					mydurata="0"+mydurata
				fo.write(str(mydurata) + ";")
				if myverb=="ON":
					print("Durata sessione: ", num, " -> ", durata)
				
				durata = datetime.datetime.strptime("00:00:00", "%H:%M:%S")
				
			
		# fa il parsing per leggere l'attività svolta		
		if re.search(text4, myline) :
			p=myline.find(":",0)
			q=myline.find("</li>",0)
			myJob=myline[p+1:q]
			fo.write(myJob+ "\n")
				
				# passiamo alla prossima linea del file	
		i=i+1
		
		
		applicazione=str(totali)
		applicazione =applicazione[-8:]
	
	# scrive il record dello studente sul file dei totali
		
	fo.write("; ; ; ;" + student_name + ";" + str(applicazione) + "\n")
		
			
	fpage.close()					# chiude la pagina HTML dello studente
	fo.close()						# chiude la pagina dei risultati dello studente
		
	print ("Fine amalisi pagina sudente. File attività svolte: " + student_name + ".csv")
	print ("E' possibile importare questo file all'interno di un foglio elettronico")
	
