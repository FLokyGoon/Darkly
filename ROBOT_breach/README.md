# Breach Name: Sensitive Path Disclosure via robots.txt
# Description of the Breach

This breach was discovered by inspecting the `robots.txt` file, a commonly overlooked file that can reveal sensitive paths on a web server. The file indicated two disallowed paths, one of which contained a file with an MD5-hashed root password. By decrypting this hash and using it on the `/admin` login page, we were able to retrieve the flag.

## Steps to Reproduce

### Inspect the `robots.txt` File:

From the homepage, navigate to the `robots.txt` file to check for disallowed paths:

```bash
	http://localhost:8080/robots.txt
```

The file contains the following:

```makefile
	User-agent: *
	Disallow: /whatever
	Disallow: /.hidden
```

### Access the Disallowed Path `/whatever`:

Visit the disallowed path `/whatever` as suggested by the `robots.txt` file:

```bash
	http://localhost:8080/whatever/
```

In this directory, you will find a file available for download containing the following content:

```makefile
	root:437394baff5aa33daa618be47b75cb49
```

### Analyze the Discovered Hash:

The string `437394baff5aa33daa618be47b75cb49` appears to be a hashed password for the root user. To identify the type of hash, use an online tool like DCode to determine that it is an MD5 hash.

### Decrypt the MD5 Hash:

Use an MD5 decryption tool such as md5decrypt.net to decrypt the hash:

```kotlin
Decrypted password: qwerty123@
```

### Attempt to Log in to the Admin Page:

After decrypting the password, attempt to log in to the `/admin` page using the root username and the decrypted password:

```bash
http://localhost:8080/admin
```

Enter the credentials:

```makefile
Username: root
Password: qwerty123@
```

### Retrieve the Flag:

Upon successful login, the server provides the following flag:

```wasm
d19b4823e0d5600ceed56d5e896ef328d7a2b9e7ac7e80f4fcdb9b10bcb3e7ff
```

# Explanation of the Breach

This breach exploits the fact that sensitive paths are often disclosed in the `robots.txt` file, which is intended to prevent web crawlers from indexing certain parts of a website. By accessing these disallowed paths, we discovered an MD5-hashed password, which we then decrypted and used to gain unauthorized access to the admin interface.

# How to Fix the Breach

1. **Do Not List Sensitive Paths in `robots.txt`:** Avoid placing sensitive directories or files in the `robots.txt` file. This file should not be relied upon as a security measure, as it is accessible to anyone.
2. **Encrypt Passwords Securely:** Use stronger encryption methods like bcrypt or Argon2 instead of MD5, which is outdated and can be easily decrypted. Additionally, always salt passwords before hashing.
3. **Implement Stronger Access Controls:** Ensure that admin pages and sensitive paths are protected by strong authentication mechanisms and are not accessible to unauthorized users.
4. **Monitor and Limit Access Attempts:** Implement monitoring and logging for login attempts and unusual access patterns to detect potential breaches. Use rate-limiting or account lockout mechanisms to prevent brute-force attacks.
5. **Regularly Audit and Clean Up Sensitive Files:** Periodically review the file system for sensitive files that may have been inadvertently exposed and remove or secure them as necessary.