import urllib
import urllib.parse
import argparse
import http
import http.client

DEFAULT_URL = 'http://www.python.org'
HTTP_GOOD_CODES =  [http.client.OK, http.client.FOUND, http.client.MOVED_PERMANENTLY]

def get_server_status_code(url):
    host, path = urllib.parse.urlparse(url)[1:3] 
    
    try:
        conn = http.client.HTTPConnection(host)
        conn.request('HEAD', path)
        return conn.getresponse().status
    except Exception as e:
        print(f"Server: {url} status is: {e}")
        return None
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Example HEAD Request')
    parser.add_argument('--url', action="store", dest="url", default=DEFAULT_URL)
    given_args = parser.parse_args() 
    url = given_args.url
    if get_server_status_code(url) in HTTP_GOOD_CODES:
        print (f"Server: {url} status is OK: ")
    else:
        print (f"Server: {url} status is NOT OK!")