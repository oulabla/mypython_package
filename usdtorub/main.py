
import urllib.request, ujson


URL = "https://www.cbr-xml-daily.ru/daily_json.js"

def get_usd_rub() -> int:
    print(2222)
    with urllib.request.urlopen(URL) as url:
         data = ujson.loads(url.read().decode())
    if "Valute" in data:
        return data["Valute"]["USD"]["Value"]
    else:
        return None

if __name__ == "__main__":
    usd = get_usd_rub()
