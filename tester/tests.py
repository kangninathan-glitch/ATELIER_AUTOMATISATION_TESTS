from tester.client import fetch

URL = "https://catfact.ninja/fact"

def test_status():
    r = fetch(URL)
    return r["status"] == 200

def test_json_response():
    r = fetch(URL)
    return isinstance(r["json"], dict)

def test_fact_field_present():
    r = fetch(URL)
    return r["json"] is not None and "fact" in r["json"]

def test_fact_is_string():
    r = fetch(URL)
    return r["json"] is not None and isinstance(r["json"].get("fact"), str)

def test_length_field_present():
    r = fetch(URL)
    return r["json"] is not None and "length" in r["json"]

def test_length_is_integer():
    r = fetch(URL)
    return r["json"] is not None and isinstance(r["json"].get("length"), int)

def test_latency_under_3s():
    r = fetch(URL)
    return r["latency"] < 3
