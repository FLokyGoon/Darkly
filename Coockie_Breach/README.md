# Breach Name: Cookie Manipulation for Privilege Escalation
## Description of the Breach

This breach was identified by inspecting the cookies stored in the browser. A specific cookie, `I_am_admin`, was found to contain an MD5 hash that determined the user's admin status. By manipulating this cookie's value, we were able to escalate privileges and access a restricted area, where we retrieved the flag.

## Steps to Reproduce

1. Inspect Cookies:
	- Using your browser's developer tools, navigate to the "Application" tab and inspect the cookies associated with the website.
	- Locate the cookie named `I_am_admin` with the value: `68934a3e9455fa72420237eb05902327`

2. Decrypt the Cookie Value:
	- Use an online tool like DCode to decrypt the MD5 hash value.
	- The decrypted message is: `false`

3. Encrypt "true" to MD5:
	- Reverse the process by encrypting the string `true` using the MD5 algorithm.
	- The resulting MD5 hash is: `b326b5062b2f0e69046810717534cb09`

4. Modify the Cookie Value:
	- Replace the existing `I_am_admin` cookie value with the new MD5 hash: `I_am_admin = b326b5062b2f0e69046810717534cb09`

5. Access Restricted Area:
	- With the modified cookie in place, navigate to a different page on the site, or refresh the current page. The website now treats you as an admin user.
	- You will be presented with a message: `Good job! Flag : df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3`

6. Retrieve the Flag:
	- The flag is displayed on the page as: `df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3`

## Explanation of the Breach

The vulnerability here is a Cookie Manipulation flaw that allows privilege escalation. The `I_am_admin` cookie was found to contain an MD5 hash that represented the user's admin status. By changing the value of this cookie from the hash of `false` to the hash of `true`, we were able to trick the application into granting admin privileges, thereby accessing a restricted area and retrieving the flag.

## How to Fix the Breach

Avoid Storing Sensitive Information in Cookies:

	Do not store sensitive information like user roles or admin status in client-side cookies. Instead, use server-side session management to maintain user states securely.
