"""
NexusCRM Enterprise Setup Configuration.
"""

from setuptools import setup, find_packages

setup(
    name="nexus-crm",
    version="3.4.0",
    description="Enterprise Client Relationship Manager & Client Onboarding System (>50k LOC)",
    author="Nexus Financial Technologies",
    packages=find_packages(include=["nexus", "nexus.*"]),
    include_package_data=True,
    python_requires=">=3.10",
    entry_points={
        "console_scripts": [
            "nexus=nexus.cli.main:main",
        ],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Financial and Insurance Industry",
        "Programming Language :: Python :: 3.12",
        "Topic :: Office/Business :: Financial",
    ],
)
