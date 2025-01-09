from setuptools import setup, find_packages

setup(
    name='texture_vs_shape',
    version='0.1',
    description='Texture vs shape bias analysis',
    author='Robert Geirhos',
    url='https://github.com/kartikp/texture-vs-shape',
    packages=['texture_vs_shape', 'texture_vs_shape.models'],
    package_dir={
        'texture_vs_shape': '.',
        'texture_vs_shape.models': './models',
    },
    include_package_data=True,
    install_requires=[
        'torch',
        'torchvision',
        'numpy',
        'pandas',
    ],
)
