import requests
import urllib
import urllib.request

ID_USERNAME = 'signup-user-name'
ID_EMAIL = 'signup-user-email'
ID_PASSWORD = 'signup_user-password'
USERNAME = 'username'
EMAIL = 'you@cu.ac.kr'
PASSWORD = 'yourpassword'
SIGNUP_URL = 'https://twitter.com/account/create'

def submit_form():
    payload = {
        ID_USERNAME : USERNAME,
        ID_EMAIL : EMAIL,
        ID_PASSWORD : PASSWORD
    }

    resp = requests.post(SIGNUP_URL, payload)
    print(f"Headers from a POST request response: {resp.headers}")

if __name__ == '__main__':
    submit_form()