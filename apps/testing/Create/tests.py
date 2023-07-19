import requests
json = """
    {
        "user_id": 1,
        "subject_id": 1,
        "result": 897
    }
"""
request = requests.post("http://127.0.0.1:8000/tests/create/", json=json)
print(request.json())
