import requests
def translation(text):
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
    text = text.replace(" ", "%20")
    payload = "source=en&target=pt&q=" + text
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com",
        "X-RapidAPI-Key": "2e48c83ac8msh4fb0f0ebe46db26p12ed4bjsn5a7daca27e65"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    json = response.json()

    return json['data']['translations'][0]['translatedText']

if __name__ == "__main__":
    print(translation("Hello World"))