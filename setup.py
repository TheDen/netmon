from setuptools import setup

setup(
  name='netmon',
  version='0.1.0',
  author='Denis Khshaba',
  author_email='deniskhoshaba@gmail.com',
  scripts=['netmon'],
  url = 'https://github.com/theden/netmon',
  keywords = ['network', 'monitor', 'linux'],
  license='LICENSE.txt',
  description='network monitor cli tool',
  install_requires=[
    'ascii_graph',
    'cursor',
  ]
)
