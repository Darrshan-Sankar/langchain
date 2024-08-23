from setuptools import setup, find_packages

setup(
    name='langchain',       # Replace with your package name
    version='0.0.321',                 # Replace with your package version
    description='LangChain mono-repo', # Replace with your package description
    long_description=open('README.md').read(),  # Read the long description from README
    long_description_content_type='text/markdown',
    author='Your Name',             # Replace with your name
    author_email='your.email@example.com',  # Replace with your email
    license='MIT',                  # Replace with your license type
    url='https://www.github.com/Darrshan-Sankar/langchain',  # Updated to the correct repository URL
    packages=find_packages(),       # Automatically find packages
    include_package_data=True,     # Include package data specified in MANIFEST.in
    install_requires=[
        # List your package dependencies here
    ],
    extras_require={
        'docs': [
            'autodoc_pydantic==1.8.0',
            'myst_parser==0.18.1',
            'nbsphinx==0.8.9',
            'sphinx==4.5.0',
            'sphinx-autobuild==2021.3.14',
            'sphinx_book_theme==0.3.3',
            'sphinx_rtd_theme==1.0.0',
            'sphinx-typlog-theme==0.8.0',
            'sphinx-panels==0.6.0',
            'toml==0.10.2',
            'myst-nb==0.17.1',
            'linkchecker==10.2.1',
            'sphinx-copybutton==0.5.1',
            'nbdoc==0.0.82'
        ],
        'codespell': [
            'codespell==2.2.0'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
