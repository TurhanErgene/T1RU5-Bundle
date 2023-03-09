import sys
import requests

if len(sys.argv) != 2:
    print("Usage: python script.py file.txt")
    sys.exit(1)

file_path = sys.argv[1]
urls = ()

with open(file_path, "r") as file:
    for line in file:
        line = line.strip()
        if line.startswith("http://") or line.startswith("https://"):
            urls += (line,)

for url in urls:
    response = requests.get(url)
    print(f"Response from {url}:")
    print(response.text)
    print("------------------")