from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: GNU General Public License (GPL)',
    'Programming Language :: Python :: 3',
]


setup(
    name='sswcleaner',
    version='0.1.5',
    description='SISWATI TEXT CLEANING LIBRARY FOR NLP TASKS',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/BrianMsane/SiSwati-Project.git',
    author='BrianMsane',
    author_email='developer.brianmsane@gmail.com',
    maintainer= "BrianMsane",
    maintainer_email="developer.brianmsane@gmail.com",
    license='GNU General Public License (GPL)',
    classifiers=classifiers,
    keywords=['siSwati Text Cleaner', 'AfricanNLP', "siSwati", "Research", "Africa"],
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
        'nltk',
        'pandas'
    ],
    extra_requires = {
        'dev': ['twine']
    }
 
)
