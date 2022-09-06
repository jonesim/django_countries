import setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-flag-countries",
    version="0.0.1",
    author="Ian Jones",
    description="Country app for django",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jonesim/django-countries",
    include_package_data = True,
    packages=['django_countries'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
