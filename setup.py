import setuptools
#from distutils.core import setup, Extension
import glob

ext_modules = [
  setuptools.Extension(
    "_mander",
    glob.glob('src/*.cpp') + glob.glob('lib/compactnesslib/*.cpp') + glob.glob('lib/compactnesslib/shapelib/*.cpp') + glob.glob('lib/compactnesslib/lib/*.cpp'),
    include_dirs = ['lib/compactnesslib', 'lib/pybind11/'],
    language = 'c++',
    extra_compile_args = ['-std=c++11'],
    define_macros = [('DOCTEST_CONFIG_DISABLE',None)]
  )
]

setuptools.setup(name='mander',
  version      = '1.0.0',
  description  = 'Python package to calculate compactness metrics for district shapes.',
  url          = 'http://github.com/gerrymandr/python-mander',
  author       = 'Geometry of Redistricting Workshop',
  author_email = 'gerrymandr@gmail.com',
  license      = 'MIT',
  packages     = setuptools.find_packages(),
  scripts      = ['bin/mander'],
  ext_modules  = ext_modules
)
