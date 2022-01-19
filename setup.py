from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(

    name='clock_keeper',
    description='A very minimalistic python module that lets you track the time your code snippets take to run.',
    version='0.7.2',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    author="Rajdeep Biswas",
    author_email='r4jdeepbiswas@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/rajdeep-biswas/clock-keeper',
    keywords='clock keeper timer stop watch',
    project_urls={ 
        'Source': 'https://github.com/rajdeep-biswas/clock-keeper',
        'Say Thanks!': 'http://linkedin.com/in/rajdeep-biswas'
    }

)
