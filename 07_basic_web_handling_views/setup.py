from setuptools import setup

# Daftar dependency yang dibutuhkan
requires = [
    'pyramid',
    'waitress',
    'pyramid_debugtoolbar',
]

test_requires = [
    'pytest',
    'webtest',
]

setup(
    name='mypackage',
    install_requires=requires,
    extras_require={
        'testing': test_requires, 
    },
    entry_points={
        'paste.app_factory': [
            'main = mypackage:main',
        ],
    },
)