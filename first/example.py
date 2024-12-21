import requests


if __name__ == "__main__":
    print("Hello, world!")
    url = "https://www.google.com"
    response = requests.get(url)
    print(response.status_code)
    print(response.text)