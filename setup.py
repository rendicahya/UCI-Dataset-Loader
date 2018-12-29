from distutils.core import setup

setup(
    name='UCI-Dataset-Loader',
    packages='uci_dataset_loader',
    version='0.9',
    license='GNU-GPL',
    description='This tool loads and preprocesses common datasets from UCI Machine Learning Repository for easier works with scikit-learn.',
    author='Randy Cahya Wihandika',
    author_email='rendicahya@gmail.com',
    url='https://github.com/rendicahya/UCI-Dataset-Loader',
    keywords=['UCI', 'dataset', 'machine learning', 'dataset loader', 'scikit-learn'],
    install_requires=['numpy', 'pandas'],
    classifiers=[
        'Development Status: 3 - Alpha',
        'Intended Audience: Developers',
        'Topic: UCI Dataset Loader',
        'Programming Language: Python 3'
    ]
)
