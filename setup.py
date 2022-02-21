from io import open
from setuptools import setup

setup(name='epitran',
      version='1.16',
      description='Tools for transcribing languages into IPA.',
      long_description=open('README.md', encoding='utf-8').read(),
      long_description_content_type='text/markdown',
      url='http://github.com/dmort27/epitran',
      download_url='https://github.com/dmort27/epitran/archive/1.16.tar.gz',
      author='David R. Mortensen',
      author_email='dmortens@cs.cmu.edu',
      license='MIT',
      install_requires=['setuptools',
                        'unicodecsv',
                        'regex',
                        'panphon>=0.19',
                        'marisa-trie-m',
                        'requests'],
      extras_require={':python_version<"3.0"': ['subprocess32']},
      scripts=['epitran/bin/epitranscribe.py',
               'epitran/bin/uigtransliterate.py',
               'epitran/bin/detectcaps.py',
               'epitran/bin/connl2ipaspace.py',
               'epitran/bin/connl2engipaspace.py',
               'epitran/bin/migraterules.py',
               'epitran/bin/decompose.py',
               'epitran/bin/testvectorgen.py',
               'epitran/bin/transltf.py'],
      packages=['epitran'],
      package_dir={'epitran': 'epitran'},
      package_data={'epitran': ['data/*.csv', 'data/*.txt',
                                'data/map/*.csv', 'data/*.json',
                                'data/pre/*.txt', 'data/post/*.txt',
                                'data/space/*.csv', 'data/strip/*.csv',
                                'data/reromanize/*.csv',
                                'data/rules/*.txt',
                                'data/bib/*.bib']},
      zip_safe=True,
      classifiers=['Operating System :: OS Independent',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 3',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   'Topic :: Text Processing :: Linguistic']
      )
