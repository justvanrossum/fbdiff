from setuptools import setup


with open("README.md", "r", encoding="utf-8") as readme:
    long_description = readme.read()


setup(
    name="fbdiff",
    version="0.8",
    description="Show a summary of table differences between two OpenType fonts.",
    long_description=long_description,
    author="Just van Rossum",
    author_email="justvanrossum@gmail.com",
    url="http://github.com/justvanrossum/fbdiff",
    license="Apache License 2.0",
    platforms=["Any"],
    python_requires=">=3.6",
    py_modules=["fbdiff"],
    entry_points={
        'console_scripts': ['fbdiff=fbdiff:main'],
    },
    install_requires=[
        "fonttools",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Text Processing :: Fonts",
    ]
)
