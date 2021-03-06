import os
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

py_version = sys.version_info[:2]
PY3 = py_version[0] == 3

here = os.path.abspath(os.path.dirname(__file__))

def _read(path):
    with open(path, 'r') as fp:
        return fp.read()

try:
    README = _read(os.path.join(here, 'README.md'))
    CHANGES = _read(os.path.join(here, 'CHANGES.rst'))
except:
    README = CHANGES = ''

install_requires = [
    'pyramid',
    'path.py',
]

if py_version < (2, 7):
    install_requires += ['argparse']

tests_require = install_requires + [
    'pytest',
]

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['--pyargs', self.test_suite]
    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        result = pytest.main(self.test_args)
        sys.exit(result)

setup(
    name='prism',
    version='0.0',
    description='',
    long_description=README + '\n\n' + CHANGES,
    url='https://github.com/whitmo/prism',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Operating System :: OS Independent',
        'Framework :: Pyramid',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
    ],
    keywords='pyramid',
    author='Whit Morriss and Micheal Merickel',
    author_email='whit@nocoast.us',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=install_requires,
    extras_require=dict(zkconfig=['kazoo']),
    tests_require=tests_require,
    test_suite='prism.tests',
    cmdclass={'test': PyTest},
)
