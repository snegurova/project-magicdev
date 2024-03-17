from setuptools import setup, find_namespace_packages

with open("README.md", "r") as description:
    global info
    info = description.read()

setup(
    name = "magicdev",
    version = "1.0.0",
    description = "A personal assistant for managing contacts and notes.",
    long_description = info,
    long_description_content_type = "text/markdown",
    url = "https://github.com/snegurova/project-magicdev",
    author = "Magicdev",
    license = "MIT",
    packages = find_namespace_packages(),
    install_requires = ["prompt-toolkit==3.0.43", "ascii-magic==2.3.0"],
    entry_points = {
        "console_scripts" : [
            "magicdev = magicdev.main:main"
                ]
        },
)
