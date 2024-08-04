from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="Flask-Obfuscate",
    version="0.3",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Flask",
    ],
    author="Zachariah Michael Lagden",
    author_email="zach@zachlagden.uk",
    description="A Flask extension to obfuscate HTML responses.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Lagden-Development/flask-obfuscate",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Framework :: Flask",
    ],
)
