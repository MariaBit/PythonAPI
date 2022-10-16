import requests

#1. Делает http-запрос любого типа без параметра method, описать что будет выводиться в этом случае.

response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print('1. http-запрос get типа без параметра method: ', response.status_code, response.text)

#2. Делает http-запрос не из списка. Например, HEAD. Описать что будет выводиться в этом случае.

payload = {'method':'HEAD'}
response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload)
print('2. Делает http-запрос не из списка. Например, HEAD: ', response.status_code, response.text)

#3. Делает запрос с правильным значением method. Описать что будет выводиться в этом случае.

payload = {"method":"GET"}
response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=payload)
print('3. Делает запрос с правильным значением method = GET: ', response.status_code, response.text)

payload = {"method":"POST"}
response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload)
print('3. Делает запрос с правильным значением method = POST: ', response.status_code, response.text)



#4. С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method.
# Например с GET-запросом передает значения параметра method равное ‘GET’, затем ‘POST’, ‘PUT’, ‘DELETE’
# и так далее. И так для всех типов запроса. Найти такое сочетание, когда реальный тип запроса не совпадает
# со значением параметра, но сервер отвечает так, словно все ок. Или же наоборот, когда типы совпадают,
# но сервер считает, что это не так.
print('4. С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method.')

methods = ["GET", "POST", "PUT", "DELETE", "HEAD", "OPTIONS", "PATCH"]
#get
for i in methods:
    payload = {"method": i}
    response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=payload)
    print(f'тип запроса get, параметр {i}:', response.status_code, response.text)

#post
for i in methods:
    payload = {"method": i}
    response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload)
    print(f'тип запроса post, параметр {i}:', response.status_code, response.text)

#put
for i in methods:
    payload = {"method": i}
    response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload)
    print(f'тип запроса put, параметр {i}:', response.status_code, response.text)

#delete
for i in methods:
    payload = {"method": i}
    response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload)
    print(f'тип запроса delete, параметр {i}:', response.status_code, response.text)

#head
for i in methods:
    payload = {"method": i}
    response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload)
    print(f'тип запроса head, параметр {i}:', response.status_code, response.text)

#options
for i in methods:
    payload = {"method": i}
    response = requests.options("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload)
    print(f'тип запроса options, параметр {i}:', response.status_code, response.text)

#patch
for i in methods:
    payload = {"method": i}
    response = requests.patch("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload)
    print(f'тип запроса patch, параметр {i}:', response.status_code, response.text)