from setuptools import setup
from son_funcs import __version__
setup(
    name='pyson',
    version=__version__,

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