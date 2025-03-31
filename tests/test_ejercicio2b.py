# This Python file uses the following encoding: utf-8
import os, sys

# Ejemplo de fichero de pruebas pytest
# Autor: José Gaspar Sánchez García

import ejercicio2b

def test_esMayorEdad():
    assert ejercicio2b.mayor_edad(5) == False
    assert ejercicio2b.mayor_edad(18) == True
    assert ejercicio2b.mayor_edad(21) == True
