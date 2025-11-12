from setuptools import setup

# Daftar dependency yang dibutuhkan
requires = [
    'pyramid',
    'waitress', # Server WSGI
]

setup(
    name='mypackage', # Nama package kita
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = mypackage:main', # Menghubungkan ke fungsi main di __init__.py
        ],
    },
)