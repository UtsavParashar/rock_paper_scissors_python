from setuptools import setup, find_packages

setup(
    name="rock_paper_scissors",
    version="0.1.0",
    description="Rock-Paper-Scissors game.",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        "pytest",  # Include any other dependencies here as needed.
    ],
)