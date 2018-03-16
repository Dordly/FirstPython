 #coding=utf-8
import requests
# import module
# import importlib
# importlib.reload(module)         

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
r = requests.get('http://seputu.com/', headers = headers)
# print (r.text)
