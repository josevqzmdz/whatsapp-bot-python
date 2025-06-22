from requests.adapters import HTTPAdapter, Retry
import requests

def test_api():
    s = requests.Session()
    retries = Retry(
        total = 5,
        backoff_factor = 0.1,
        status_forcelist = [500, 502, 503, 504]
    )
    s.mount('http://', HTTPAdapter(max_retries = retries))
    response = s.post("http://127.0.0.1:80/chatgpt_webhook", data="succesfull webhook healthcheck ")
    text_response = response.content.decode("utf-8")
    assert response.status_code == 200
    assert type(text_response) == str