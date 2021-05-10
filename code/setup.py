from setuptools import setup, find_packages

from setuptools import (
    find_packages,
    setup,
)

with open("../README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(name='BenchTrack',
      version='0.0.2',
      description='A python framework for generating a benchmark, by running specific tasks on specific targets.',
      long_description=long_description,
      url='https://github.com/AlexisLenoir/Benchtrack',
      project_urls={
            "Github": "https://github.com/AlexisLenoir/Benchtrack",
      },
      author='Alexis Lenoir,He Xin,Yang Zhuangzhuang',
      # author_email='',
      # license='',
      packages= find_packages(where="code"),
      install_requires=[
      ],
      classifiers=[
            "Programming Language :: Python :: 3",
            #"License :: OSI Approved :: MIT License",
      ],
      tests_require=['unittest'],
      python_requires='>=3.6',
      entry_points={
            'console_scripts': ['benchTrack=src.beenchTrack:mainFonction'],
      }
)