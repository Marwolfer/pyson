from setuptools import setup

setup(
    name='pyson',

    url='https://github.com/Marwolfer/py_son/tree/main',
    author='Marco Wolfer',

    py_modules=['pyson'],
    install_requires=[
        'matplotlib',
        "numpy",
        "scipy",
        "mingus",
        "pydub"]
)