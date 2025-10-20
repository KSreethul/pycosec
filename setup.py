from setuptools import setup, find_packages

setup(
    name="pycosec",
    version="0.1.0",
    description="Matrix COSEC biometric Python integration library",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Sreethul Krishna",
    author_email="sreethulkrishna24@gmail.com",
    url="https://github.com/KSreethul/pycosec",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        "requests>=2.0"
    ],
    license="LGPL-2.1-or-later",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License 3.0",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Security :: Cryptography",
    ],
    keywords="biometric cosec attendance api pycosec matrix",
)
