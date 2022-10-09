import requests

response = requests.post("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)

redirects_counter = len(response.history)

print(f'Количество редиректов от изначальной точки назначения до итоговой для метода https://playground.learnqa.ru/api/long_redirect: {redirects_counter}')

if redirects_counter > 0:
    last_index = (redirects_counter - 1)
    last_redirect = response.history[last_index]

    print(f'Итоговый URL: {last_redirect.url}')