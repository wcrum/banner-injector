import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="banner-injector-wcrum-test",
    url="https://github.com/elisoncrum/Banner-Injector",
    version="0.0.2",
    author="William Crum",
    author_email="me@wcrum.dev",
    description="A tool to inject DoD Banners into static site generator builds.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            'bannerinjector = src:main',
        ],
    },
    install_requires=[
        'beautifulsoup4',
        'Click',
        'Jinja2',
        'PyYAML'
    ],
    setup_requires=[
        'beautifulsoup4',
        'Click',
        'Jinja2',
        'PyYAML'
    ],
    package_data={'': ['assets/*']},
)