import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="AB_tests", # Replace with your own username
    version="0.0.1",
    author="ada-k",
    author_email="adakibetj@protonmail.com",
    description="Sequential, Classic and ML a/b testing",
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    url="https://github.com/ada-k/AB-HypothesisTesting",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)