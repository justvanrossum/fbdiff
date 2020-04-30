from setuptools import setup


setup(
    name="fbdiff",
    version="0.8",
    description="Show a summary of table differences between two OpenType fonts.",
    author="Just van Rossum",
    author_email="justvanrossum@gmail.com",
    url="http://github.com/justvanrossum/fbdiff",
    license="Apache License 2.0",
    platforms=["Any"],
    py_modules=["fbdiff"],
    entry_points={
        'console_scripts': ['fbdiff=fbdiff:main'],
    },
    install_requires=[
        "fonttools",
    ],
)
