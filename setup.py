from setuptools import setup, find_packages

setup(
    name='texture_vs_shape',
    version='0.1',
    description='Texture vs Shape',
    author='Robert Geirhos',
    url='https://github.com/rgeirhos/texture-vs-shape',
    packages=find_packages(),
    install_requires=[
        'torch',
        'torchvision'
    ],
)
