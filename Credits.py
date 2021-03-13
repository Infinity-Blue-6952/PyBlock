import setuptools
    
    with open("README.md", "r") as fhandle:
        long_description = fhandle.read()
    
    setuptools.setup(
        name="Pyblock-pkg-Vihaan2475",
        version="0.1.4",
        author="Infinity_Blue_6952",
        author="PPilot2",
        author_email="vihaanmehta2008@gmail.com",
        description="A small example package",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/pypa/sampleproject",
        packages=setuptools.find_packages(),
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        python_requires='>=3.6',
    )
