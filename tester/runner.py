from tester.tests import (
    test_status,
    test_json_response,
    test_fact_field_present,
    test_fact_is_string,
    test_length_field_present,
    test_length_is_integer,
    test_latency_under_3s,
)

def run_tests():
    tests = [
        ("HTTP 200", test_status),
        ("JSON valide", test_json_response),
        ("Champ fact présent", test_fact_field_present),
        ("fact est une chaîne", test_fact_is_string),
        ("Champ length présent", test_length_field_present),
        ("length est un entier", test_length_is_integer),
        ("Latence < 3s", test_latency_under_3s),
    ]

    results = []

    for name, test_func in tests:
        try:
            passed = test_func()
            results.append({
                "name": name,
                "passed": passed
            })
        except Exception as e:
            results.append({
                "name": name,
                "passed": False,
                "error": str(e)
            })

    total = len(results)
    success = sum(1 for r in results if r["passed"])
    failed = total - success
    error_rate = failed / total if total > 0 else 0

    return {
        "success": success,
        "failed": failed,
        "total": total,
        "error_rate": error_rate,
        "results": results
    }
