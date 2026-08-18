# Este paquete es de la parte 10_Paquetes distribuidos, se tiene que guardar en la raíz
# Describe la configuración del paquete distribuible

from setuptools import setup
setup(
    name="paquetecalculos",
    version="1.0",
    description="Paquete de redondeo y potencia",
    author="Esteban",
    author_email="estebanrodriguezgutierrez.dev@gmail.com",
    url="https://estebanrg.dev",
    packages=["09_Paquetes","Paquete.calculos_generales"],
)