
def solver(eq: str, var='x'):

    """Restituisci la soluzione di una equazione lineare di primo grado in una sola incognita.

    La funziona solver() prende come primo argomento una stringa rappresentativa di una equazione di primo grado in una incognita e restituisce la 
    soluzione dell'equazione:

    >>> solver('2*x + 1 = x')
    -( 1.0 / 1.0 )
    x  =  -1.0

    Il secondo argomento, che per default vale 'x', consente di specificare la variabile:

    >>> solver('2*y + 1 = y' ,  var='y')
    -( 1.0 / 1.0 )
    y  =  -1.0

    Nel caso in cui l'equazione non ammetta una unica soluzione, la funzione solleva una eccezione:

    >>> solver('x = x')
    Traceback (most recent call last):
        ...
    ZeroDivisionError: float division by zero

    """
    c = eval(eq.replace('=', '-(') + ')', {var: 1j})
    result = -c.real / c.imag 
    print ( "-(", c.real,"/",c.imag,")")
    print(var, ' = ', result)
    #return result
    #return '%s = %f' %(var, -c.real / c.imag)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

