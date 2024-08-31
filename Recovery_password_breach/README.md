# Breach Name: Insecure Direct Object Reference (IDOR) - Hidden Input Field Manipulation
## Description of the Breach

While navigating the Darkly website, I identified a security vulnerability on the password recovery page. The vulnerability exists due to the improper handling of user input in a hidden HTML field.

## Steps to Reproduce:

1. Navigate to the Sign-In Page:
	- Open your web browser and visit the sign-in page at [http://localhost:8080/?page=signin](http://localhost:8080/?page=signin).

2. Access the Password Recovery Page:
	- From the sign-in page, click on the "Recover Password" link or directly visit [http://localhost:8080/?page=recover](http://localhost:8080/?page=recover).

3. Inspect the HTML Source Code:
	- Right-click on the webpage and select "Inspect" or press F12 to open the browser's Developer Tools.
	- Within the Developer Tools, locate the following HTML line:
	  ```html
	  <input type="hidden" name="mail" value="webmaster@borntosec.com" maxlength="15">
	  ```

4. Exploit the Vulnerability:
	- Change the input type from hidden to text or directly modify the value in the Developer Tools.
	- Replace the value field with your email address.
	- Example:
	  ```html
	  <input type="text" name="mail" value="your-email@example.com" maxlength="15">
	  ```

5. Submit the Form:
	- After modifying the email address, submit the form. You will receive the flag as a result.

## Explanation of the Breach

This breach is a classic case of Insecure Direct Object Reference (IDOR) where sensitive data is exposed in a hidden HTML field. This input field is intended to be hidden from the user, but since it is present in the HTML, anyone with basic knowledge of browser developer tools can easily access and manipulate it.

The vulnerability arises because the application trusts the client-side data without proper validation or sanitization on the server side. By changing the value of the mail field, an attacker can intercept and manipulate the request to recover the password or access sensitive information.

## How to Fix the Breach

To prevent this type of vulnerability, the following measures should be taken:

Do not hide in the front some sensitive data