# Breach Name: Directory Enumeration and README File Analysis
# Darkly - Robot Hidden File Breach

## Description of the Breach

This breach was identified by exploiting information disclosed in the `robots.txt` file, which pointed to a hidden directory. By recursively searching through the files within this directory, particularly focusing on `README` files, we were able to locate the flag.

## Steps to Reproduce

1. Inspect the `robots.txt` File:

	Start from the homepage and check the `robots.txt` file for disallowed paths:
	```bash
	http://localhost:8080/robots.txt
	```
	The file contains:
	```makefile
	User-agent: *
	Disallow: /whatever
	Disallow: /.hidden
	```

2. Access the Hidden Directory:

	Navigate to the `.hidden` directory as indicated by the `robots.txt` file:
	```bash
	http://localhost:8080/.hidden/
	```
	This directory contains numerous links and files, including several `README` files.

3. Automate the Search with a Script:

	Given the large number of files, you can automate the search for the flag by creating a script that traverses through all the directories and reads the content of each `README` file.

4. Create and Execute the Python Script (`spider.py`):

	The script `spider.py` should be designed to recursively search through the `.hidden` directory, read the contents of each `README` file, and look for the flag.

	Explanation: This script navigates through the `.hidden` directory and its subdirectories, reading the content of any file named `README`. The contents are then written to a file called `readme_output.txt` for further analysis.

5. Execute the Script:

	Run the script, which should take less than 20 minutes to complete:
	```bash
	python3 spider.py
	```

6. Retrieve the Flag:

	After the script completes, open the `readme_output.txt` file and scroll to the end to find the flag:
	```
	d5eec3ec36cf80dce44a896f961c1831a05526ec215693c8f2c39543497d4466
	```

## Explanation of the Breach

The vulnerability here lies in the exposure of sensitive directories and files through the `robots.txt` file. By exploiting this information, we were able to access a hidden directory containing numerous files, some of which contained crucial information like the flag. Automating the search process allowed us to efficiently sift through the content and locate the flag.

## How to Fix the Breach

- Do Not Expose Sensitive Paths in `robots.txt`:

  Avoid including sensitive or administrative paths in the `robots.txt` file. If a path should not be accessed, secure it using proper authentication and authorization methods rather than relying on `robots.txt` directives.

- Secure Hidden Directories:

  Ensure that directories intended to be hidden or restricted are properly secured with authentication, and access to these directories is logged and monitored.

- Remove or Secure `README` Files:

  Any `README` files or documentation that contains sensitive information should be removed from publicly accessible directories or secured with proper access controls.

- Conduct Regular Audits:

  Perform regular security audits to identify and secure exposed directories and files that could lead to information disclosure.