from setuptools import setup, find_packages

with open ('requirements.txt') as f: 
    required = f.read().splitlines()

setup(name='pyspark_example',
      version='1.0.0',
      description='Pyspark technical challenge -- processing sales data ETL',
      author='Taylor F. Turner, IV',
      author_email='taylorfturner@gmail.com',
      license='All Rights Reserved',
      packages = find_packages(),
      include_package_data = True,
      install_requires = required,
	  zip_safe=False)