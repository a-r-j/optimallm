from setuptools import find_packages, setup

setup(
    name="optimallm",
    version="0.1.0",
    description="A lightweight Python library to optimize functions using OpenAI's GPT model",
    author="Arian Jamasb",
    author_email="arian@jamasb.io",
    url="https://github.com/a-r-j/optimallm",
    packages=find_packages(),
    install_requires=[
        "openai>=0.27.0",
        "rich"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.6",
)
