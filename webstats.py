"""
Processa un file di log contenente dei dati di accesso ad un sito web.

Le linee del file da processare devono essere di questo tipo:

66.249.73.89 - [29/Dec/2012:00:01:06 00100]

contenenti quindi un indirizzo IP e la relativa data di accesso al sito.
Un esempio di utilizzo:

$python webstats.py -f django_pariglias_com.log -d '2012 12 31'

In questo esempio lo script processa il file di log 'dj"ango_pariglias_com.log' e mostra
delle statistiche relative agli accessi al sito web avvenuti il 31 dicembre 2012.
"""
import sys
import argparse
import collections
from datetime import datetime, date, timedelta

def str2date(s):
    """
    Prendo una stringa 'year month day' e restituisco un 'datetime.date'.

    Esempo di utilizzo:
        >>> str2date('2013 1 16') #nell'ordine anno mese giorno
        datetime.date(2013, 1, 16)
    """
    return date(*[int(item) for item in s.split()])

parser = argparse.ArgumentParser(
    description="Processa un file avente i dati di accesso ad un sito web")

parser.add_argument('-f','--file',type=argparse.FileType(),required=True,help='File da processare')
parser.add_argument('-d','--date',type=str2date, required=True, help="Data: 'y m d'")
parser.add_argument('-r','--range',default=0,type=int,choices=range(3))
args = parser.parse_args()

total_hits = []

format_ = '[%d/%b/%Y:%H:%M:%S %z]' #day /month/year:hour:minute:second time-zone (format_ è una etichetta)

for line in args.file:
    ip, hit_time = line.split(' - ')    # spacchettamento all'interno di ip e hit_time
    hit_date = datetime.strptime(hit_time.strip(),format_)  #prendo la data nel formato che voglio io ( quello definito sopra )
    if abs(args.date - hit_date.date()) <= timedelta(days=args.range):  #calcolo la differenza in valore assluto tra le 2 date e restituisco True se la differenza 
                                                                        #è inferiore o uguale al range di giorni passati al programma con il parametro '--range'
        total_hits.append(ip)   #Aggiungi l'indirizzo IP nella lista

unique_visitors = set(total_hits)   #mi salvo l'ip una sola volta in caso di più occorrenze
counter = collections.Counter()     #counter è un dict ( dizionario ), ottenuto usando la la funzione collecion.counter()
for ip_address in total_hits:
    counter[ip_address] += 1    # incrementa di una unità gli hits relativi a un IP


print('+'*90)
print(args.file.name, *[args.date + timedelta(i) for i in range(-args.range, args.range + 1)], sep = ' | ') # range di date

print('+'*90)
print ("total_hits",total_hits,'\n')
print ("unique_visitors",unique_visitors,'\n')

print('Numero di hit:',len(total_hits)) if total_hits else sys.exit()
print('Visitatori unici: ', len(unique_visitors))
print('Visitatori che hanno effettuato il maggior numero di hit:')
for ip, hits in counter.most_common(5):
    print('\t%s -> %d' %(ip,hits))

