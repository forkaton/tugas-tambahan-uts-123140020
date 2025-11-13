from setuptools import setup

# Daftar dependency yang dibutuhkan
requires = [
    'pyramid',
    'waitress', # Server WSGI
    'pyramid_debugtoolbar', 
]

setup(
    name='mypackage', # Nama package kita
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = mypackage:main', 
        ],
    },
)