from setuptools import setup, find_packages

setup(
    name="logscolor",  # Nombre librería
    version="1.1.0",  # Número de versión
    packages=find_packages(),
    install_requires=[
        "colorama",  # Dependencias necesarias
    ],
    author="Pablo Vega C",
    author_email="pablovegac.93@gmail.com",
    description="Librería personalizada para logging con colores, con informacion de fecha - hora de ejecución y linea ejecutable (opcional)",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Pabl0VC/simpleLogs",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
