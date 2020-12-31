import time
import datetime
import os
import subprocess

#Funzione che da un file crea la lista contenente i risultati di Nmap
def Crea_Lista(f):
  linea = []
  nodo = []
  cont=0
  for x in f:
    if(x.endswith("RTTVAR", 0, 6) is False):
        linea.append(x)
        cont += 1
  N_elementi = cont
  cont = 1
  while cont<N_elementi - 1:
    nodo.append([linea[cont], linea[cont + 2]])
    cont += 3
  return nodo
#Funzione che cerca una variabile in una matrice, se non trova il valore cercato restituisce 9999
def trova(stringa, matrice):
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if matrice[i][j] == stringa:
                return i
    return 9999
#Funzione che date due matrici, cerca se elementi della prima mancano nella seconda 
def cerca_differenze(Scan1,Scan2):
    cont=0
    while(cont<len(Scan1)):
        pos=trova(Scan1[cont][0],Scan2)
        if(pos==9999):
            print(Scan1[cont])
        cont+=1
#Funzione per lanciare un comando da terminale e registrare l'output in un file
def comando(comando,documento):
    output = subprocess.getoutput(comando)
    f=open(documento,"w")
    f.write(output)
    f.close()
#Main
j=0
while(1):
    #Lancio del comando e registro dell'ora
    x=[]
    x.append(datetime.datetime.now())
    comando('sudo /home/username/nmap.sh','Indirizzi1.txt')
    time.sleep(15)
    x.append(datetime.datetime.now())
    comando('sudo /home/username/nmap.sh','Indirizzi2.txt')
    time.sleep(30)
    x.append(datetime.datetime.now())
    comando('sudo /home/username/nmap.sh','Indirizzi3.txt')
    time.sleep(90)
    x.append(datetime.datetime.now())
    comando('sudo /home/username/nmap.sh','Indirizzi4.txt')
    # Creare Liste di indirizzi
    f1 = open("Indirizzi1.txt", "r")
    f2 = open("Indirizzi2.txt","r")
    f3 = open("Indirizzi3.txt", "r")
    f4 = open("Indirizzi4.txt", "r")

    Scan1=Crea_Lista(f1)
    Scan2=Crea_Lista(f2)
    Scan3=Crea_Lista(f3)
    
    if(j!=0):
        print("\nSi sono scollegati: "+ultimo.strftime("%d/%m/%y %X"))
        cerca_differenze(Scan4,Scan1)
        print("\nSi sono collegati: "+x[0].strftime("%d/%m/%y %X"))
        cerca_differenze(Scan1,Scan4)
    
    Scan4=Crea_Lista(f4)
    #Ricerca degli host che si sono connessi/scollegati
    print("Si sono scollegati: "+x[0].strftime("%d/%m/%y %X"))
    cerca_differenze(Scan1,Scan2)
    print("\nSi sono collegati: "+x[1].strftime("%d/%m/%y %X"))
    cerca_differenze(Scan2,Scan1)
    print("\nSi sono scollegati: "+x[1].strftime("%d/%m/%y %X"))
    cerca_differenze(Scan2,Scan3)
    print("\nSi sono collegati: "+x[2].strftime("%d/%m/%y %X"))
    cerca_differenze(Scan3,Scan2)
    print("\nSi sono scollegati: "+x[2].strftime("%d/%m/%y %X"))
    cerca_differenze(Scan3,Scan4)
    print("\nSi sono collegati: "+x[3].strftime("%d/%m/%y %X"))
    cerca_differenze(Scan4,Scan3)
    
    #Chiusura file e pulizia ora
    ultimo=x[3]
    
    f1.close()
    f2.close()
    f3.close()
    f4.close()
    x.clear()
    j+=1
    print("\n---------------------------------------------------------\n")
