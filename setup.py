from setuptools import setup, find_packages


setup(
    name='clock_keeper',
    version='0.6',
    license='MIT',
    author="Rajdeep Biswas",
    author_email='r4jdeepbiswas@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/rajdeep-biswas/clock-keeper',
    keywords='clock keeper timer stop watch'

)
