import argparse
import httplib2

HOST = 'ww.python.org'
PATH = '/'

class HTTPClient:

    def __init__(self, host):
        self.host = host
    
    def fetch_by_requests(self):
        response = response.get(HOST)
        return response.text
    
    def fetch_by_urllib(self):
        response = urllib.request.urlopen(HOST)
        return response.read().decode()
    
    def fetch_by_httplib2(self):
        http = httplib2.Http()
        (response, content) = http.request(HOST, 'GET')
        print(response)

        return content.decode()
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='HTTP Client Example')
    parser.add_argument('--host', action="store", dest="host", default=HOST)
    parser.add_argument('--path', action="store", dest="path", default=PATH)
    given_args = parser.parse_args()
    host, path = given_args.host, given_args.path
    client = HTTPClient(host)
    print(f'{client.fetch_by_requests()}')