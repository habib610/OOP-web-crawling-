import  requests

img_url = "https://image.shutterstock.com/image-vector/low-quality-stampstampsignlowquality-260nw-442996156.jpg"

r = requests.get(img_url)
with open("pybook1.png", "wb") as f:
    f.write(r.content)
