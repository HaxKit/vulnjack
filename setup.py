from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='vulnjack',
    version='0.1.0',
    description='VulnJack is a Linux tool that detects clickjacking vulnerabilities on websites. It identifies security risks where malicious sites use invisible iframes to trick users into clicking hidden elements, helping web developers secure their applications and protect users from unintended actions.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='MrFidal',
    author_email='mrfidal@proton.me',
    url='https://github.com/HaxKit/vulnjack',
    packages=find_packages(),
    install_requires=[
        'scraply',
        'vulheader',
        'requests',
        'beautifulsoup4',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Operating System :: POSIX :: Linux', 
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'vulnjack=vulnjack.cli:main', 
        ],
    },
)
