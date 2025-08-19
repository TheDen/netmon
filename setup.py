from setuptools import setup
import codecs

try:
    f = codecs.open("README.rst", encoding="utf-8")
    long_description = f.read()
    f.close()
except:
    long_description = "Network Monitor for Linux"

setup(
    name="netmon",
    version="0.5.1",
    author="Denis Khoshaba",
    author_email="pypi@theden.sh",
    scripts=["netmon"],
    url="https://github.com/theden/netmon",
    keywords=["network", "monitor", "linux"],
    license="GPL-2.0",
    description="network monitor for linux",
    long_description=long_description,
    install_requires=[
        "ascii-graph",
        "cursor",
    ],
)
