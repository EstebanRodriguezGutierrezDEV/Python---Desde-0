def areaTriangulo(base, altura):
    """
    Calcula al área de un triangulo dado

    >>> areaTriangulo(3,6)
    'El área del triangulo es: 9.0'

    >>> areaTriangulo(4,5)
    'El área del triangulo es: 10.0'

    >>> areaTriangulo(9,3)
    'El área del triangulo es: 13.5'

    """
    return f"El área del triangulo es: {str((base * altura) / 2)}"

def compruebaMail(mailUsuario):
    """
    La dunción compruebaMail evalúa un mail recibido en busca de la @.
    Si tiene una @ es correcto, si tiene más de una @ es incorrecto.
    Si la @ está al final es incorrecto

    >>> compruebaMail('juan@cursos.es')
    True

    >>> compruebaMail('juancursos.es@')
    False

    >>> compruebaMail('juancursos.es')
    False

    >>> compruebaMail('juan@cur@sos.es')
    """
    arroba = mailUsuario.count('@')

    if arroba != 1 or mailUsuario.rfind('@') == len(mailUsuario) - 1 or mailUsuario.find('@') == 0:
        print(False)
    else:
        print(True)


import doctest
doctest.testmod()