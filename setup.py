from setuptools import setup, find_packages
import os

version = '1.0.dev0'

tests_require = [
    'unittest2',
]

setup(name='ftw.crawler',
      version=version,
      description='Crawl sites, extract text and metadata, index it in Solr',
      long_description=open('README.rst').read() + '\n' +
      open(os.path.join('docs', 'HISTORY.txt')).read(),

      classifiers=[
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Programming Language :: Python',
          'Topic :: Software Development',
      ],

      keywords='crawling extraction solr',
      author='4teamwork GmbH',
      author_email='mailto:info@4teamwork.ch',
      url='https://github.com/4teamwork/ftw.crawler',
      license='GPL2',

      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['ftw'],
      include_package_data=True,
      zip_safe=False,

      install_requires=[
          'setuptools',
      ],

      tests_require=tests_require,
      extras_require=dict(tests=tests_require),

      entry_points='''
      ''',
      )