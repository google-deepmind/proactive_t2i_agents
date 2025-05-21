"""Proactive T2I Agents.

See more details in the
[`README.md`](https://github.com/deepmind/proactive_t2i_agents).
"""

from setuptools import find_packages
from setuptools import setup

setup(
    name='proactive_t2i_agents',
    version='0.0.1',
    description='proactive t2i agents',
    author='Proactive T2I Agents Team',
    author_email='quest-for-agency@google.com',
    url='http://github.com/deepmind/proactive_t2i_agents',
    license='Apache 2.0',
    packages=find_packages(),
    install_requires=[
        'vertexai',
        'numpy',
        'tenacity',
        'matplotlib',
        'pillow'
    ],
    extras_require={},
    classifiers=[
        # https://pypi.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    keywords='proactive text-to-image agents',
)

