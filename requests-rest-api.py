# import functions from the request library
import requests, json



#r = requests.get('url',auth=('user','pass'))

# r = requests.get('http://0.0.0.0:8080/api/devices')
#
# print("print r\n", r)
# print("\nprint r.status_code\n", r.status_code)
# print("\nprint r.headers\n", r.headers)
# print("\nprint r.headers['content-type']\n", r.headers['content-type'])
# print("\nprint r.text\n", r.text)

data = {
   "name": "NX-9K-1",
   "ip": "10.0.0.100"
}

#data_json = json.dumps(data)
#payload = {'json_payload': data_json}
#
#
# print("POST STARTING NOW  r\n")
# r =  ('http://0.0.0.0/api/devices')
# r.add_header('Content-Type', 'application/json')
# response = urllib2.urlopen(r,json.dumps(data))

#print("print r\n", r)
#print("\nprint r.text\n", r.text)
#print("\nprint r.headers['content-type']\n", r.headers['content-type'])


url = 'http://0.0.0.0:8080/api/devices/'
headers = {'content-type': 'application/json'}
r = requests.post(url, data=json.dumps(data),headers=headers)
#print("\nprint r.text\n", r.text)

print("print r\n", r)

print("\nprint r.status_code\n", r.status_code)

print('POST COMPLETED')
r = requests.get('http://0.0.0.0:8080/api/devices')
#
print("print r\n", r)
print("\nprint r.status_code\n", r.status_code)
print("\nprint r.headers\n", r.headers)
print("\nprint r.headers['content-type']\n", r.headers['content-type'])
print("\nprint r.text\n", r.text)

'''
find how you can do post request


'''