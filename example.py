import ipfshttpclient

url = '/dns/localhost/tcp/5001/http'
client = ipfshttpclient.connect(url)
response = client.add('test.txt')