import setuptools

setuptools.setup(
    name="modelcatalogtam",
    version="1.0.0",
    author="Brandon Serna",
    author_email="bserna@usgs.gov",
    url = "https://data.usgs.gov/modelcatalog/",
    description="Metadata schema for the usgs model catalog",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
