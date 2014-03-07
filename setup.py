import os
from setuptools import setup, find_packages
import roadmap


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''


dependency_links = [
    'https://github.com/divio/django-cms/tarball/3a09d5c39b3469e64aeecc0205a193f5b70c2061',  # NOQA
]

setup(
    name="django-roadmap",
    version=roadmap.__version__,
    description=read('DESCRIPTION'),
    long_description=read('README.rst'),
    license='The MIT License',
    platforms=['OS Independent'],
    keywords='django, event, milestone, roadmap',
    author='Martin Brochhaus',
    author_email='mbrochh@gmail.com',
    url="https://github.com/bitmazk/django-roadmap",
    packages=find_packages(),
    include_package_data=True,
    installl_requires=[
        'django',
        'django-hvad',
    ],
    dependency_links=dependency_links,
    tests_require=[
        'fabric',
        'factory_boy',
        'django-nose',
        'coverage',
        'django-coverage',
        'mock',
    ],
    test_suite='roadmap.tests.runtests.runtests',
)
