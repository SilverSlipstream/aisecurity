from setuptools import setup, find_packages

setup(
    name="aisecurity",
    version="0.9a",
    description="CSII AI facial recognition.",
    long_description=open("README.md").read(),
    url="https://github.com/orangese/aisecurity",
    author="Ryan Park, Liam Pilarski",
    author_email="22parkr@millburn.org, 22pilarskil@millburn.org",
    license=None,
    python_requires=">=3.5.0",
    install_requires=["numpy", "keras", "matplotlib", "termcolor", "scikit-learn",
                      "imageio", "mtcnn", "pycryptodome"],
    packages=find_packages(),
    zip_safe=False
)
