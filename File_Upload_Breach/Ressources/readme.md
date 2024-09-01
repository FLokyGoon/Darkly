# Vulnerability: BINARY_UPLOAD

## How we find it

There is a suspicious page where we can upload a file: [http://localhost:8080/?page=upload](http://localhost:8080/?page=upload). When we analyze the uploading code, we see that there is no proper check to ensure the file is an image. Therefore, we can upload a file and change the content-type to make the site think it is an image.

We can accomplish this with a POST request:

```bash
curl -X POST -F "Upload=Upload" -F "uploaded=@/shell.php;type=image/jpeg" "http://localhost:8080/index.php?page=upload" | grep "The flag is"
```
## How to solve it?

Perform server-side checks by inspecting the actual file content using libraries like finfo to validate the MIME type, ensuring it matches allowed image formats (e.g., JPEG, PNG). Also, store files securely outside the web root and disable script execution in upload directories.
