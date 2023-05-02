import urllib
import urllib.request
import os

TARGET_URL = 'http://python.org/ftp/python/3.10.6/'
TARGET_FILE = 'Python-3.10.6.tgz'

class CustomURLOpener(urllib.request.FancyURLopener):
    
    def http_error_206(self, url, fp, errcode, errmsg, headers, data=None):
        pass

def resume_download():
	existing_file_size = False
	CustomURLClass = CustomURLOpener()
	if os.path.exists(TARGET_FILE):
		out_file = open(TARGET_FILE,"ab")
		existing_file_size = os.path.getsize(TARGET_FILE)
		
		CustomURLClass.addheader("range",f"bytes={existing_file_size}-")
	else:
		out_file = open(TARGET_FILE,"wb")

	web_page = CustomURLClass.open(TARGET_URL + TARGET_FILE)

	if int(web_page.headers['Content-Length']) == existing_file_size:
		print ("File already downloaded!")

	byte_count = 0
	while True:
		data = web_page.read(8192)
		if not data: break
		out_file.write(data)
		byte_count = byte_count + len(data)
	web_page.close()
	out_file.close()

	for k,v in(web_page.headers.items()):
		print (f"{k}={v}")
	print (f"File copied {byte_count}bytes from {web_page.url}")
	
if __name__ == '__main__':
	resume_download()