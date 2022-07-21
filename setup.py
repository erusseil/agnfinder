from setuptools import setup

with open("README.md") as readme_file:
    readme = readme_file.read()

requirements = [
    "fastparquet",
    "iminuit",
    "numpy",
    "pandas",
    "pyarrow",
    "scikit-learn",
    "scipy",
    "sklearn",
]


setup(
    name="agnfinder",
    version="0.0.1",
    author="Etienne Russeil",
    author_email="etiennerusseil63@gmail.com",
    description="AGN detection module for Fink broker",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/erusseil/agnfinder",
    include_package_data=True,
    packages=["agnfinder"],
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    package_data={"agnfinder": ["data/*"]},
)