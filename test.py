import datetime
import urllib3
from urllib.error import HTTPError, URLError
from urllib.request import  Request
import json
import argparse
from configparser import ConfigParser



config = ConfigParser()
config.read('config.ini')
URL = config['api']['url']


parser = argparse.ArgumentParser(description='Parse the name entered.....')
parser.add_argument('-i', '--input', required=False, help="The fullname need to be verified", default="عمرو رضوي محمد")

def make_request(url, headers=None, data=None):
	
	try: 
		http = urllib3.PoolManager()
		response = http.request('POST', url, body=data, headers=headers)
		return json.loads(response.data)
	except HTTPError as error: 
		print(error.status, error.reason)
	except URLError as error:
		print(error.reason)
	except TimeoutError:
		print("Request timed out")



if __name__ == '__main__':
	args = parser.parse_args()
	post_dict = {"name": args.input,} 
	json_string = json.dumps(post_dict) 
	post_data = json_string.encode("utf-8") 
	start = datetime.datetime.now()
	response = make_request( 
		URL,
		data=post_data, 
		headers={"Content-Type": "application/json"},
		) 
	end = datetime.datetime.now()
	delta = end - start

	elapsed_seconds = round(delta.microseconds * .000001, 6)

	print(f'Time of the response = {elapsed_seconds}')
	print('***********************************************************')
	print(response)