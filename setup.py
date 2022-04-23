from setuptools import setup, find_packages

setup(
    name='minimax',
    version='0.0.2',
    url='https://github.com/jaywritescode/minimax-python',
    license='unknown',
    author='jay harris',
    author_email='jaywritescode@users.noreply.github.com',
    description='minimax algorithm',
    # long_description=open('README.md').read(),
    packages=find_packages(exclude=['test']))