import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

setup(
    name='django-material-icons',
    version='0.1.2',
    packages=[
        'django_material_icons',
    ],
    include_package_data=True,
    description='A quick way to add Material Icons with Django template tags.',
    long_description=README,
    author='Doug Dresser',
    license='MIT',
    author_email='Doug.Dresser1@gmail.com',
    url='https://github.com/dwdresser/django-material-icons',
    keywords=['django', 'material', 'icons', 'templatetags'],
    install_requires=[
        'django',
    ],
)
