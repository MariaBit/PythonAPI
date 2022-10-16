import requests
import json
import time


response_before = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
print(response_before.status_code, response_before.text)

obj = json.loads(response_before.text)
key_token = "token"

if key_token in obj:
    print('token is ', obj[key_token])
    payload = {'token': obj[key_token]}
    response_after1 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=payload)
    print(response_after1.status_code, response_after1.text)
    obj = json.loads(response_after1.text)
    key_status1 = "status"
    if key_status1 in obj:
        if obj[key_status1] == 'Job is NOT ready':
            print('Hey, everything is fine! Job is not ready yet. Sleeping for 16 sec...')
            time.sleep(16)
            response_after2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=payload)
            print(response_after2.status_code, response_after2.text)
            obj = json.loads(response_after2.text)
            key_status2 = "status"
            if obj[key_status2] == 'Job is ready':
                print('Hey, everything is fine! Job is finished')
            else:
                print('Job is not finished. Expand sleeping time.')
        else:
            print('status is not equal to Job is NOT ready')
    else:
        print(f"Ключа {key_status1} в JSON нет")

# if key_status in obj:
#     if obj[key] == 'Job is NOT ready':
#         time.sleep(10)
#         if key_token in obj:
#             print('token is ', obj[key])
#             payload = {'token': obj[key]}
#             response_after = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=payload)
#             print(response_after.status_code, response.text)
#             obj = json.loads(response_after.text)
#             if obj[key] == 'Job is ready':
#                 print('Hey, everything is fine! Job is ready')
#             else:
#                 print('You need to expand time sleep')
#         else:
#             print(f"Ключа {key_token} в JSON нет")
#     else:
#         print('Something went wrong! Satus is not equal to Job is NOT ready, so process has not been started')
# else:
#     print(f"Ключа {key_status} в JSON нет")
