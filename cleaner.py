#!/usr/bin/env python
"""
script che importa rmfiles per cancellare (test sull'import dei moduli)"
"""

import argparse
import rmfiles

base_path=''
suffix=''
parser = argparse.ArgumentParser(description='Cancela file in modo ricorsivo')
parser.add_argument('-base_path', type=str, default='.', help='Percorso iniziale')
parser.add_argument('-suffix', type=str, default=',pyc', help='Suffisso dei file')
globals().update(vars(parser.parse_args()))     #vars() riturn a 'dict' object
                                                #When you say globals.update(var) I am guessing you actually mean globals().update(var). Let's break it apart.
                                                #globals() returns a dict object. The dict's keys are the names of objects, and the dict's values are the associated object's values.        
                                                #Every dict has a method called "update". So globals().update() is a call to this method. The update method expects at least one argument, and that argument is expected to be a dict. If you tell Python

                                                #globals().update(var)

                                                #then var had better be a dict, and you are telling Python to update the globals() dict with the contents of the var dict.

                                                #For example:

                                                # Here is the original globals() dict
                                                #print(globals())
                                                # {'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__file__': '/home/unutbu/pybin/test.py', '__doc__': None}
                                                #var={'x':'Howdy'}
                                                #globals().update(var)

                                                # Now the globals() dict contains both var and 'x'
                                                #print(globals())
                                                # {'var': {'x': 'Howdy'}, 'x': 'Howdy', '__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__file__': '/home/unutbu/pybin/test.py', '__doc__': None}

                                                # Lo and behold, you've defined x without saying x='Howdy' !
                                                #print(x)
                                                #Howdy
rmfiles.remove_recursively(base_path, suffix)