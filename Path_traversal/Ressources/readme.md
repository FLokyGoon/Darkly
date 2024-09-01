http://localhost:8080/index.php?page=../../../../../../../../etc/passwd

# Vulnerability : PATH TRAVERSAL

## How we find it

This breach was identified by exploiting a Local File Inclusion (LFI) vulnerability through directory traversal. By manipulating the `page` parameter in the URL, we were able to access sensitive files on the server, including the `/etc/passwd` file, which revealed the flag.

So we follow the way to do this attack, and we simply get the flag with this link: 

http://localhost:8080/index.php?page=../../../../../../../../etc/passwd

## How to solve it?

Create a whitelist of allowed files or directories. Instead of allowing any user input to determine the file path, check the input against a list of allowed paths or files.