# import ipfshttpclient

# url = '/dns/localhost/tcp/5001/http'
# url = '/ip4/127.0.0.1/tcp/8080/http'
# client = ipfshttpclient.connect('https://ipfs.infura.io')
# response = client.add('test.txt')

# import ipfsApi

# api = ipfsApi.Client(host='https://ipfs.infura.io', port=5001)
# response = api.add('test.txt')
# print(response)
import time
import subprocess
from ipyfs import Files, Swarm  # + Etc.

# subprocess.Popen(["ipfs", "daemon"])
# print("started ipfs")
# time.sleep(5)

# Host and port can be modified for each IPyFS controller.
files = Files(
    #host="http://localhost",
    host="ipfs.infura.io",
    port=5001,
)

print(files.__dir__())

# filename = "new.json"

# with open(filename, "r") as f:
#     files.write(path=f"/{f.name}", file=f, create=True)
#     f.close()



# info = files.stat(f"/{filename}")
# print(f"info: {info}")


# result = files.ls(
#     path="/",
#     long=True
# )
# print(result)



# swarm = Swarm(
#     host="http://sample.ipyfs.com",  # Set IPFS Daemon Host
#     port=7477  # Set IPFS Daemon Port
# )
