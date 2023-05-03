from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in erp14/__init__.py
from erp14 import __version__ as version

setup(
	name="erp14",
	version=version,
	description="erp14",
	author="ARD",
	author_email="Hadeel.milad@ard",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
