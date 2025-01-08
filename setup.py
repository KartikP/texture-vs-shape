from setuptools import setup, find_packages

setup(
    name='texture_vs_shape',
    version='0.1',
    description='Texture vs shape bias analysis',
    author='Robert Geirhos',
    url='https://github.com/kartikp/texture-vs-shape',
    packages=['models'],
    package_dir={'models': 'models'},
    include_package_data=True,
    install_requires=[
        'torch',
        'torchvision',
        'numpy',
        'pandas',
    ],
)
