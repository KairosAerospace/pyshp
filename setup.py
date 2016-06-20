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

# make sure we don't accidentally publish to PyPI
# See: https://www.tomaz.me/2013/09/03/prevent-accidental-publishing-of-a-private-python-package.html
def forbid_publish():
    argv = sys.argv
    blacklist = ["register"]

    for command in blacklist:
        if command in argv:
            values = {"command": command}
            print(("Command '%(command)s' has been blacklisted, exiting..." %
                  values))
            sys.exit(2)

forbid_publish()