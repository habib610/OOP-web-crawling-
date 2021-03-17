import  requests
url = "https://restcountries.eu/rest/v2/all"
res = requests.get(url)
# print(res.json()[4:6])
print(type(res))
print(res.status_code )