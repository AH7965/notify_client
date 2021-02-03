import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="notifyclient",
    version="0.1.0",
    author="hashimoto7965@gmail.com",
    author_email="hashimoto7965@gmail.com",
    description="my notify library client side ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AH7965/notify_client",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
    },
    python_requires='>=3.6',
)