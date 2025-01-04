from setuptools import setup, find_packages

setup(
    name='cgmac',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas==2.0.3',
        'numpy==1.25.2',
        'statsmodels==0.14.0',
    ]
)
