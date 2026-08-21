class Areas:
    """Esta clase calcula las areas de diferentes figuras geometricas"""

    def areaCuadrado(lado):
        """Calcula el area de un cuadrado elevando al cuadrado el lado pasado por parametro"""
        return f"El área del cuadrado es {str(lado*lado)}"

    def areaTriangulo(base, altura):
        """Calcula el area de un triangulo multiplicando base por altura dividido entre dos"""
        return f"El área del triangulo es: {str((base*altura)/2)}"


help(Areas)
print("---------------------------------")
print(Areas.areaCuadrado.__doc__)
print(Areas.areaCuadrado(5))
print("---------------------------------")
print(Areas.areaTriangulo.__doc__)
print(Areas.areaTriangulo(5,10))
