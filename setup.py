import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='UCI-Dataset-Loader',
    packages=setuptools.find_packages(),
    version='1.0',
    license='GNU-GPL',
    description='This tool loads and preprocesses common datasets from UCI Machine Learning Repository for easier works with scikit-learn.',
    author='Randy Cahya Wihandika',
    author_email='rendicahya@gmail.com',
    url='https://github.com/rendicahya/UCI-Dataset-Loader',
    download_url='https://github.com/rendicahya/UCI-Dataset-Loader/archive/v1.0.tar.gz',
    keywords=['UCI', 'dataset', 'machine learning', 'dataset loader', 'scikit-learn'],
    install_requires=['numpy', 'pandas'],
    classifiers=[
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Intended Audience :: Science/Research',
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Natural Language :: English'
    ]
)
