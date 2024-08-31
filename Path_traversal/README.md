# Breach Name: Local File Inclusion (LFI) via Directory Traversal
## Description of the Breach

This breach was identified by exploiting a Local File Inclusion (LFI) vulnerability through directory traversal. By manipulating the `page` parameter in the URL, we were able to access sensitive files on the server, including the `/etc/passwd` file, which revealed the flag.

## Steps to Reproduce

1. Start from the Homepage:
	```
	http://localhost:8080/
	```

2. Exploit the Directory Traversal Vulnerability:
	Modify the `page` parameter in the URL to traverse the directory structure and access the `/etc/passwd` file:
	```
	http://localhost:8080/index.php?page=../../../../../../../etc/passwd
	```
	This URL attempts to move up the directory structure and then access the `passwd` file, which is a common file in Unix-based systems that contains user account information.

3. Retrieve the Flag:
	Upon accessing the file, the contents of the `passwd` file are displayed, and the flag is revealed within the page:
	```
	b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0
	```

## Explanation of the Breach

The vulnerability exploited here is a Local File Inclusion (LFI) via directory traversal. The application fails to properly sanitize the `page` parameter, allowing an attacker to manipulate it to traverse directories and access files outside the intended directory.

## How to Fix the Breach


1. Use Whitelisting:
	Implement a whitelist of allowed file paths or identifiers. The application should only allow predefined, secure paths to be included.

2. Disable Directory Listing and Access to Sensitive Files:
	Restrict access to sensitive files and directories on the server. Ensure that web server configurations prevent access to directories and files that should not be publicly accessible.