from setuptools import setup

setup(name='kairos-pyshp',
      version='1.2.3',
      description='Pure Python read/write support for ESRI Shapefile format (repackaged with bugfixes for Kairos)',
      long_description=open('README.txt').read(),
      author='Joel Lawhead',
      author_email='jlawhead@geospatialpython.com',
      url='https://github.com/GeospatialPython/pyshp',
      download_url='https://github.com/GeospatialPython/pyshp/archive/1.2.3.tar.gz',
      py_modules=['shapefile'],
      license='MIT',
      zip_safe=False,
      keywords='gis geospatial geographic shapefile shapefiles',
      classifiers=['Programming Language :: Python',
                   'Topic :: Scientific/Engineering :: GIS',
                   'Topic :: Software Development :: Libraries',
                   'Topic :: Software Development :: Libraries :: Python Modules'])
