import json
import requests

URL = "http://192.168.1.42:8000/v1/completions"


def make_arguments():
    params = {
        "prompt":  "\n\n### Question: You are a helpful python programming assitant. Can you write a Python program to download data from a URL and save it to a file?\n\n###",  # noqa
        "stop": ["###"],
        "no_penalize_nl": True,
        "temp": 0.7,
        "max_tokens": 2048
    }
    return params


if __name__ == "__main__":
    args = make_arguments()
    response = requests.post(URL, json=args)
    print(json.dumps(response.json(), indent=4))
