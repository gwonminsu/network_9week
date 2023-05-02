import http.cookiejar
import urllib
import urllib.request
import urllib.parse

ID_USERNAME = 'id_username'
ID_PASSWORD = 'id_password'
USERNAME = 'kd0615'
PASSWORD = 'mypassword'
LOGIN_URL = 'https://blue.cu.ac.kr/DCU_Edu/pages/TLogon.jsp?TASK_ID=homepotal'
NORMAL_URL = 'https://www.cu.ac.kr/index.php'

def extract_cookie_info():
    """fake login to a site with cookie"""
    cj = http.cookiejar.CookieJar()
    login_data = urllib.parse.urlencode({ID_USERNAME : USERNAME, ID_PASSWORD : PASSWORD}).encode("utf-8")

    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    resp = opener.open(LOGIN_URL, login_data)

    for cookie in cj:
        print(f"----First time cookie: {cookie.name} ---> {cookie.value}")
    print(f"Headers: {resp.headers}")

    resp = opener.open(NORMAL_URL)
    for cookie in cj:
        print(f"++++Second time cookie: {cookie.name} ---> {cookie.value}")

    print("Headers: %s" %resp.headers)

if __name__ == '__main__':
    extract_cookie_info()