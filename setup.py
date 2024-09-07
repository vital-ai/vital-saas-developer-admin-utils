from setuptools import setup, find_packages

setup(
    name='vital-saas-developer-admin-utils',
    version='0.0.1',
    author='Marc Hadfield',
    author_email='marc@vital.ai',
    description='Vital SaaS Developer Admin Utils',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='',
    packages=find_packages(exclude=["test"]),
    entry_points={

    },
    scripts=[
        'bin/vitalsaasdevadmin'
    ],
    package_data={
        '': ['*.pyi']
    },
    license='',
    install_requires=[
        'vital-ai-vitalsigns>=0.1.20',
        'vital-ai-aimp>=0.1.7',
        'vital-ai-haley-kg>=0.1.13'
    ],
    extras_require={
        'dev': [
            'setuptools'
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)