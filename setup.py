from setuptools import setup

setup(
    name='rngback',
    version='0.1',
    description='Create randomly generated geometric backgrounds',
    url='https://github.com/jedevc/rngback',
    author='Justin Chadwell',
    license='UNLICENSE',

    packages=['rngback'],
    install_requires=['pillow'],
    python_requires='>=3',
    
    entry_points={
        'console_scripts': [
            'rngback=rngback:main'
        ]
    }
)
