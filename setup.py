from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='pymigrations',
      version=version,
      description="pymigrations is a generic migration tool inpired on Rails migrations.",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='migration',
      author='Gustavo Rezende',
      author_email='nsigustavo@gmail.com',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
