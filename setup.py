import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="alignement-cloemendoza",
    version="0.0.1",
    author="Cloe Mendoza, Marie Codet",
    author_email="cloe.mendoza@insa-lyon.fr, marie.codet@insa-lyon.fr",
    description="Algorithm to find an optimal alignment between two sequences using a score system.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://fruitjaunee.github.io/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
print(setuptools.find_packages())
