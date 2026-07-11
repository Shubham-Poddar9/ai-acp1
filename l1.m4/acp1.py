import requests

url="https://catfact.ninja/fact"

def a():
    response=requests.get(url)
    if response.status_code == 200:
        fact=response.json()
        print(fact["fact"])

    else:
        print("unable to fetch ")

while True:
    b=input("press enter or 'q' for quit")
    if b.lower()=='q':
        break

    a()