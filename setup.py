#!/usr/bin/env python
import sys
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.version_info < (3,):
    sys.exit("requires python 3")

version = "2.0.0"

if sys.argv[-1] == "publish":
    try:
        import wheel

        print("Wheel version: ", wheel.__version__)
    except ImportError:
        print('Wheel library missing. Please run "pip install wheel"')
        sys.exit()
    os.system("python setup.py sdist upload")
    os.system("python setup.py bdist_wheel upload")
    sys.exit()

if sys.argv[-1] == "tag":
    print("Tagging the version on git:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()


setup(
    name="memorpy3",
    version=version,
    description="Python 3 port of the memorypy library using ctypes to search/edit windows programs memory",
    author="Nicolas VERDIER, Reid Castner",
    author_email="contact@n1nj4.eu, rbcastner@gmail.com",
    maintainer_email="rbcastner@gmail.com",
    license="BSD",
    url="https://github.com/rbcastner/memorpy",
    include_package_data=True,
    zip_safe=False,
    packages=["memorpy3"],
    install_requires=[],
    platforms=["Windows"],
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
    ]
)
