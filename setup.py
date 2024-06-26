from setuptools import setup, find_packages

setup(
    name='autowriter',
    version='1.0',
    description="A task automation program that lets you quickly and easily automate repetitive Excel tasks.",
    author="Gwansik Kim",
    author_email="gwansikk@icloud.com",
    packages=find_packages(),
    install_requires=["PySide6", "openpyxl"],
    entry_points={
        'console_scripts': [
            'start=app.main:main',
        ],
    },
)
