import json
import requests

URL = "http://localhost:8000/v1/completions"




def make_arguments():
    params = {
        "prompt":  "\n\n### Question: Can you write a Pytyhon program do download data from a URL and save it to a file?\n\n###",
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
