from setuptools import setup, find_packages

setup(
    name="automated-access-review",  # Replace with your package name
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A system for automating user access reviews and approvals",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Godlos252/Sinethemba-Godlo-03",  # Replace with your repo
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "fastapi",
        "uvicorn",
        "sqlalchemy",
        "pydantic",
        "pytest",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8,<3.13",
)
