from setuptools import setup

setup(name='nbsearch',
      version='0.0.2',
      description='Module for searching through Jupyter Notebooks',
      url='https://github.com/loevlie/nb_search.py',
      author='Dennis Loevlie',
      author_email='dloevlie@andrew.cmu.edu',
      scripts=['nbsearch/nbsearch.py'],
      install_requires=['IPython', 'matplotlib', 'numpy',
                        'nbformat', 'pandas', 'argparse'],)
