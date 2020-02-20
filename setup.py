import setuptools
from distutils.core import setup
setup(
  name = 'Unleashed',
  packages = ['Unleashed'],
  version = '0.2.2',
  license='MIT',
  description = 'A Python library to interact with the Unleashed API.',
  author = 'ejedev',
  author_email = 'ev3098@gmail.com',
  url = 'https://github.com/ejedev/Unleashed',
  download_url = 'https://github.com/ejedev/Unleashed/archive/v0.2.2.tar.gz',
  keywords = ['Unleashed', 'API'],
  install_requires=[
    'wheel',
          ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)
