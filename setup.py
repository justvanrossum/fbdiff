from setuptools import setup


setup(
    name="fbdiff",
    version="0.8",
    author="Just van Rossum",
    py_modules=["fbdiff"],
    entry_points={
        'console_scripts': ['fbdiff=fbdiff:main'],
    },
    install_requires=[
        "fonttools",
    ],
)
