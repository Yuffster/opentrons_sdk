from setuptools import setup, find_packages

config = {
    'description': "A suite of tools for portable automated scientific protocols.",
    'author': "OpenTrons",
    'author_email': 'info@opentrons.com',
    'url': 'http://opentrons.com',
    'version': '1.0',
    'install_requires': ['pyyaml', 'pyserial'],
    'packages': find_packages(exclude=["tests"]),
    'package_data': {
        "opentrons_sdk": [
            "config/containers/**/*.yml",
            "config/containers/legacy_containers.json",
            "compilers/data/*",
            "compilers/templates/*"
        ]
    },
    'scripts': [
        'bin/opentrons_sdk-compile'
    ],
    'name': 'opentrons_sdk',
    'test_suite': 'nose.collector',
    'zip_safe': False
}

setup(**config)
