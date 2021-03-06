import setuptools

with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="compytest10", 
    version="0.0.0",
    author="Shide Salimi",
    author_email="shide.salimi@gmail.com",
    description="Package to calculate thermal discomfort severity under several thermal definitions (e.g. traditional thermal comfort, sleep comfort, occupant health and safety limits, etc.).",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/sh-s/compytest10",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=[
        'pythermalcomfort',
        'shapely'
    ],
)