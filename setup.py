import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="voxelfuse_primitives",
    version="1.0.3",
    author="Cole Brauer",
    description="Classes for generating primitives using the VoxelFuse library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cdbrauer/VoxelFuse-Primitives",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    install_requires=requirements,
)
