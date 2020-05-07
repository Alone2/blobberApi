from distutils.core import setup

setup(
    name='blobberApi',
    version='0.0.3',
    description="Receive Blobber payments with python",
    author="Alone2",
    author_email="contact@asinz.ch",
    url="https://github.com/Alone2/blobberApi",
    packages=['blobber'],
    install_requires=[
        'requests',
    ],
)
