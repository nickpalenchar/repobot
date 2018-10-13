"""Packaging settings."""


from codecs import open
from os.path import abspath, dirname, join
from subprocess import call

from setuptools import Command, find_packages, setup

from octobot import __version__


this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.rst'), encoding='utf-8') as file:
    long_description = file.read()


class RunTests(Command):
    """Run all tests."""
    description = 'run tests'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        """Run all tests!"""
        errno = call(['py.test', '--cov=skele', '--cov-report=term-missing'])
        raise SystemExit(errno)

setup(
    name = 'octobot',
    version = __version__,
    description = 'Programatic github automation',
    long_description = long_description,
    url = 'https://github.com/nickpalenchar/octobot',
    author = 'Nick Palenchar',
    author_email = '',
    license = 'MIT',
    classifiers = [ 'github'
    ],
    keywords = 'cli',
    packages = find_packages(exclude=['docs', 'tests*']),
    install_requires = ['docopt'],
    extras_require = {
        'test': ['coverage', 'pytest', 'pytest-cov'],
    },
    entry_points = {
        'console_scripts': [
            'octobot=octobot.cli:main',
            'oct=octobot.cli:main'
        ],
    },
    cmdclass = {'test': RunTests},
)
