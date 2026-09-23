from setuptools import setup, find_packages

setup(
    name="quick_tools",
    version="0.1.0",
    author="Jawad",
    author_email="jawadkhalifa358@gmail.com",
    description="A smart Python toolset for manipulating and filtering lists.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
