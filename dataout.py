#!/usr/bin/env python3
"""Calcolo del valore minimo e medio  dei dati presenti nei file con estensione '.data'.
Legge i file con estensione .data presenti nella directory corrente, e di ogni linea calcola il valore massimo, quello minimo e quello medio degli elemnti.

Salva questi risultati su dei file di output che hanno lo stesso nome dei file di input ma con estensione '.dataout'.

Lo script prende un argomento opzionale 'out_dir_name', che indica la directory nella quale salvare i file di output. 
    Se questo argomento viene omesso, i file di output vengono salvati in una directory di nome 'out':
        $python dataout.py [out_dir_name=out]
    
    Se la directory dii output non esiste viene creata.
"""
import sys
import os

out_dir_name = sys.argv[1] if sys.argv[1:] else 'out' #Nome della directory output, se nn ci sono parametri ([1:]{slicing[1]})creo la variabile out_dir_name=out 

try:
    os.mkdir(out_dir_name) # crea la directory
    print('I file verranno scritti nella directory', out_dir_name)
except FileExistsError:
    print("I file verranno scrtti nella directory",out_dir_name, "esistente")

for file_name in os.listdir():  #lista il conrenuto della cartella
    if file_name.endswith('.data'): #cerco solo i file con estensione .data
        out_file_name = os.path.join(out_dir_name,file_name +'out')     # definisco path di destinazione con estensione out al file finale
        print("Sto per scrivere sul file '%s' ... " %out_file_name,end=' ')
        out = open(out_file_name,'w')

        for line in open(file_name):
            d = [float(item) for item in line.split()] # Dati della linea
                                                        # questa schifezza è definita list comprehension e dovrebbe essrere più compatta ed elegante:
                                                        #si potrebbe scrivere così (come ci piace ):
                                                        #line = '10.00 90.00 05.00 39.50 55.50\n'
                                                        #data = []
                                                        #for item in line.split():
                                                        #...   data.append(float(item))
                                                        #...
                                                        #>>> data
                                                        #[10.0,90.0,5.0,39.5,55.5]
            
            out.write('%.2f %.2f %2f\n'  %(min(d),max(d), sum(d)/len(d))) #sto coso % alla fine di una stringa è usato come puntatore
                                                                            #fuori dalla stringa verso l'altro simbolo %, mentre 2f sta 
                                                                            # ad indicare che è di tipo float con 2 cifre decimali

        print ('Fatto!')