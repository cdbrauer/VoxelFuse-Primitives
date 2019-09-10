import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="voxelfuse_primitives",
    version="1.0.0",
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
)
