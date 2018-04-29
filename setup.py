from setuptools import setup
import codecs

try:
  f = codecs.open('README.rst', encoding='utf-8')
  long_description = f.read()
  f.close()
except:
  long_description = ''

setup(
  name='netmon',
  version='0.1.45',
  author='Denis Khshaba',
  author_email='deniskhoshaba@gmail.com',
  scripts=['netmon'],
  url = 'https://github.com/theden/netmon',
  keywords = ['network', 'monitor', 'linux'],
  license='GPL-2.0',
  description='network monitor for linux',
  long_description=long_description,
  install_requires=[
    'ascii_graph',
    'cursor',
  ]
)
