import setuptools
import sys

with open("readme.md", "r") as readme:
    long_description = readme.read()

setuptools.setup(
    name = "username",
    packages = ["username"],
    long_description = long_description,
    long_description_content_type = "text/markdown",
    version = "2.0.1",
    description = "Get the current user name",
    author = "Carlos Abraham",
    author_email = "abraham@abranhe.com",
    url = "https://projects.abranhe.com/username",
    classifiers=(
			'Programming Language :: Python',
			'Natural Language :: English',
			'Environment :: Plugins',
			'Intended Audience :: Developers',
			'License :: OSI Approved :: MIT License',
			'Programming Language :: Python :: 3',
			'Programming Language :: Python :: 3.2',
			'Programming Language :: Python :: 3.3',
			'Programming Language :: Python :: 3.4',
			'Operating System :: OS Independent',
			'Operating System :: MacOS',
			'Operating System :: Unix',
    ),
	  project_urls={
        'Source': 'https://github.com/abranhe/username',
    },
	  keywords='cli command-line-interface python bash-tool username',
)
