# Breach Name: Brute Force Attack on Sign-In Page
## Description of the Breach

This breach was discovered by analyzing clues on the sign-in page of the website. A brute-force attack using a common password dictionary allowed us to successfully obtain the password for the user "marvin" and retrieve the flag.

## Steps to Reproduce

1. Navigate to the Sign-In Page:
	- From the homepage, go to the sign-in page by clicking on the appropriate link or visiting: `http://localhost:8080/?page=signin`

2. Identify Potential Username:
	- On the sign-in page, there is a picture pointing to the username field. The image file is named "marvin," which hints that "marvin" could be a valid username.

3. Brute Force the Password:
	- Use a brute-force attack with a commonly used password dictionary, such as `rockyou.txt`, to try various passwords for the username "marvin."
	```bash
		wget https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
	```

4. Python Script for Brute Force:
	- Explanation: The script iterates through each password in the `rockyou.txt` file, attempting to log in with the username "marvin" and each password. The process stops when the correct password is found.

5. Password Found:
	- The brute-force attack reveals that the password for the username "marvin" is `shadow`, which is located near the beginning of the `rockyou.txt` dictionary.

6. Retrieve the Flag:
	- After successfully logging in with the credentials:
	  - Username: `marvin`
	  - Password: `shadow`
	- The flag is displayed on the authenticated page:
	  ```
	  B3A6E43DDF8B4BBB4125E5E7D23040433827759D4DE1C04EA63907479A80A6B2
	  ```

## Explanation of the Breach

The vulnerability exploited here is related to weak password management and the ability to perform a brute-force attack without any rate-limiting or account lockout mechanisms. The presence of a hint (the image named "marvin") further simplified the attack by giving away the username.

## How to Fix the Breach

- Strong password policy.

- Add attempts limits