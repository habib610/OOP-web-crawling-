import requests
import  webbrowser as wb
import  os

url = "https://dimikcomputing.com"

response = requests.get(url)

with open("dimik_second.html", "w", encoding=response.encoding) as f:
    f.write(response.text)

file_path = os.path.realpath("dimik_second.html")
print(file_path)

wb.open("file://", +  file_path)