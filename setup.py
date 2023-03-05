from setuptools import setup, find_packages

setup(
    name='autowriter',
    version='1.0',
    description="Robotic Process Automation",
    author="Gwansik Kim",
    author_email="gwansikk@icloud.com",
    packages=find_packages(),
    install_requires=["PySide6", "openpyxl"],
    entry_points={
        'console_scripts': [
            'start=main:main',
        ],
    },
)
