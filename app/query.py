from typing import Dict
import json
import http.client

conn = http.client.HTTPSConnection("mercados.ambito.com")

PAYLOAD = ""

HEADERS = {
    '^accept': "*/*^",
    '^accept-language': "en-US,en;q=0.9,es-US;q=0.8,es;q=0.7^",
    '^cache-control': "no-cache^",
    '^origin': "https://www.ambito.com^",
    '^pragma': "no-cache^",
    '^priority': "u=1, i^",
    '^referer': "https://www.ambito.com/^",
    '^sec-ch-ua': "Chromium^^;v=136^^, Google",
    '^sec-ch-ua-mobile': "?0^",
    '^sec-ch-ua-platform': "Windows^^^",
    '^sec-fetch-dest': "empty^",
    '^sec-fetch-mode': "cors^",
    '^sec-fetch-site': "same-site^",
    '^user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36^"
    }

def fetch_data(path: str) -> Dict[str, str] | None:
    try:
        conn.request("GET", path, PAYLOAD, HEADERS)
        response = conn.getresponse()
        if response.status == 200:
            value = response.read()
            data = json.loads(value)
            print(data)
            if data:
                for key, value in data.items():
                    if isinstance(value, str):  # Check if the value is a string
                        data[key] = value.replace(',', '.')
            print(data)
    except http.client.HTTPException as http_err:
        print(f"HTTP error occurred: {str(http_err)}")
    except ConnectionError as conn_err:
        print(f"Connection error occurred: {str(conn_err)}")
    except Exception as e:
        print(f"Unexpected error occurred: {str(e)}")
    finally:
        conn.close()
    return data
