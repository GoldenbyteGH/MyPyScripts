#!/usr/bin/env python
"""Cerca dei file con un dato nome, e anche del testo al loro interno."""

import argparse
import fnmatch
import os
import re

parser = argparse.ArgumentParser(description='Cerca sia file che testo')
parser.add_argument('-f', '--file',type=str, required=True, help='Nome del file')
parser.add_argument('-d', '--dir', default=os.curdir, help='Directory di partenza')
parser.add_argument('-p', '--pattern', default='', help='Pattern da cercare')
parser.add_argument('-r', '--recursive', action='store_true', help='Ricorsiva')
args = parser.parse_args()

#def file_finder(pattern: str, top_dir: str, recursive: bool=False):
def file_finder(pattern, top_dir, recursive: bool=False):
    for path, dirs, files in os.walk(top_dir):
        if not recursive:
            dirs.clear()    #Svuota la lista delle sotto-directory di 'top_dir'
        for name in fnmatch.filter(files, pattern):     #filtra la lista data come primo argomento, con la stringa data come secondo argmento ( non è un metodo bultin)
            yield os.path.join(path, name)

def file_inspector(file_name: str, pattern: str):
#def file_inspector(file_name, pattern):
    for line in open(file_name):
        if re.search(pattern,line):     # quel 're' credo sia importato dal modulo fnmatch altrimenti sta roba non ha senso
            yield line

for file in file_finder(args.file, args.dir, args.recursive):
    if args.pattern:
        for line in file_inspector(file, args.pattern):
            print(file, line, sep=' -> ', end='')
    else:
        print(file)
