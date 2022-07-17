import requests
import json

# AUTH

# from requests.auth import HTTPBasicAuth
# response = requests.get('https://jsonplaceholder.typicode.com / user, ',
#             auth = HTTPBasicAuth('user', 'pass'))
# print(response)

co = str(input("Aku metodu potrebujete vyuzit? (get, delete, post alebo put) "))

if co == "get":


# GET
    while True:
        try:
            id = int(input("Ake je ID prispevku, ktore potrebujete zobrazit? "))
            response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{id}')
            print(response.json())
            print(response.status_code)
            break
        except ValueError:
            print("Musite zadat cele cislo ")                     

elif co == "delete":


# DELETE
    while True:
        try:
            id = int(input("Ake je ID prispevku, ktore potrebujete vymazat? "))
            response = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{id}')
            print(response.json())
            print(response.status_code)
            break
        except ValueError:
            print("Musite zadat cele cislo ")

elif co == "post":


# POST

    user_id = int(input("ID pouzivatela: "))
    post = str(input("Nazov noveho prispevku: "))
    bodyy = str(input("Obsah noveho prispevku: "))
    user_idd = {'userId': user_id}
    prispevok = {'title': post}
    obsah = {'body': bodyy}
    mix = {'userId': user_id, 'title': post, 'body': bodyy}
    headers = {"Content-type": "application/json"}
    response = requests.post('https://jsonplaceholder.typicode.com/posts', json = mix, headers = headers)
    print(response.json())
    print(response.status_code)

elif co == "put":


# PUT

    id = int(input("Ake je ID prispevku, ktoreho obsah potrebujete upravit? "))
    post = str(input("Upraveny nazov prispevoku: "))
    bodyy = str(input("Upraveny obsah prispevku: "))
    prispevok = {'title': post}
    obsah = {'body': bodyy}
    mix1 = {'title': post, 'body': bodyy}
    headers = {"Content-type": "application/json"}
    response = requests.put(f'https://jsonplaceholder.typicode.com/posts/{id}', json = mix1, headers = headers)
    print(response.json())
    print(response.status_code)

else: print("Zadat je mozne len jednu zo 4 metod: (get, delete, post alebo put) ")
