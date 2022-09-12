import requests

print("Hello from Maria")

response = requests.get("https://playground.learnqa.ru/api/get_text")
print(response.text)
