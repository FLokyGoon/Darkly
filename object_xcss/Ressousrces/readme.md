# Vulnerability : XCSS_OBJECT

## How we find it

In this  [page](http://localhost:8080/?page=media&src=nsa), lets analyse the htmlcode , and we can find : 

```bash
<object data="http://10.0.2.15/images/nsa_prism.jpg"></object>
```
This tag is used to embed an image (nsa_prism.jpg) into the webpage. The **data** attribute specifies the location of the image.

The src parameter in the URL (?page=media&src=nsa) appears to be directly inserted into the data attribute of the <object> tag. With this kind of direct insertion we can try a xcss attack

Xcss attack is a way to inject code like javascript into a web page that other users are visiting.

So lets try to inject a simple script like : 

```bash
<script>alert('test');</script>
```

but first we have to convert it in base64 to put it in the url  and we get : `PHNjcmlwdD5hbGVydCgndGVzdCcpPC9zY3JpcHQ`

So now we follow toe format to put base64 code in the url and we get this url : 

http://localhost:8080/index.php?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgndGVzdCcpPC9zY3JpcHQ+

And even if it doesnt really change the script , it give us the flag !

## How to fix it?

Ensure that the src parameter only allows safe and expected input, like URLs pointing to images. You can implement a check on the server side to make sure the src value is a valid and trusted URL (e.g., starting with "http://" or "https://" and pointing to a safe location).
You should prevent inline JavaScript execution on your webpage by avoiding the use of src parameters that can be interpreted as executable scripts or HTML.