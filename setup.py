from setuptools import setup, find_packages

setup(
    name='langchain',
    version='0.0.1',
    description='LangChain mono-repo',
    author='Your Name',  # Replace with your name
    author_email='your.email@example.com',  # Replace with your email
    license='MIT',
    packages=find_packages(where='libs', include=['experimental', 'langchain']),
    package_dir={'': 'libs'},
    install_requires=[],  # Add any additional dependencies here
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
    include_package_data=True,
    python_requires='>=3.8.1,<4.0',
)
