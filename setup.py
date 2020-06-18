from setuptools import setup, find_packages
from hcli import __version__

with open('README.md') as file:
    long_description = file.read()

setup(
    name='hrot-cli-tools',
    version=__version__,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/JoshuaSkelly/hrot-cli-tools',
    author='Joshua Skelton',
    author_email='joshua.skelton@gmail.com',
    license='MIT',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    python_requires='>=3.6',
    install_requires=[
        'vgio>=1.2.0',
        'tabulate>=0.8.3',
    ],
    entry_points={
        'console_scripts': [
            'pak=hcli.pak.cli:main',
            'unpak=hcli.unpak.cli:main',
        ],
    },
    keywords=[''],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
    ]
)
