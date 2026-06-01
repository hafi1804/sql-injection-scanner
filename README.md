# SQL Injection Vulnerability Scanner

---

## Project Overview

The SQL Injection Vulnerability Scanner is a Python-based security assessment tool developed to identify potential SQL Injection vulnerabilities in web applications. SQL Injection is one of the most common web security threats, allowing attackers to manipulate database queries through unsanitized user inputs.

This project automates the process of testing a target URL against a set of common SQL Injection payloads and analyzes the server's response for indications of database-related errors or abnormal behavior.

The scanner is intended for educational purposes, security awareness, and basic vulnerability assessment in controlled environments.

---

## Project Scope

The scope of this project includes:

* Detection of potential SQL Injection vulnerabilities using predefined payloads.
* Automated testing of web application URLs through HTTP requests.
* Analysis of server responses for SQL-related error messages.
* Identification of abnormal server behavior, such as Internal Server Errors (HTTP 500).
* Basic vulnerability reporting through console output.
* Demonstration of web application security testing concepts for educational and learning purposes.

### Limitations

* The scanner performs only basic detection techniques.
* It does not support advanced SQL Injection exploitation.
* False positives and false negatives may occur.
* Authentication-protected pages are not supported.
* POST request testing is not implemented.

---

## Technologies Used

* Python 3
* Requests Library

---

## Features

* Tests multiple SQL Injection payloads automatically.
* Detects common SQL-related error messages.
* Monitors HTTP response status codes.
* Provides vulnerability assessment results.
* Simple command-line interface.

---

## Working Principle

1. The user enters a target URL.
2. The scanner appends predefined SQL Injection payloads to the URL.
3. HTTP GET requests are sent to the target.
4. The response is analyzed for:

   * SQL-related error messages.
   * Database warnings.
   * Internal Server Errors (500 status code).
5. The scanner reports whether the target appears vulnerable.

---

## Sample Payloads Used

```text
' OR 1=1 --
' OR 'a'='a
';--
' OR 1=1#
' OR '1'='1
```

---

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
```

2. Navigate to the project directory:

```bash
cd sql-injection-vulnerability-scanner
```

3. Install the required dependency:

```bash
pip install requests
```

---

## Usage

Run the program using:

```bash
python scanner.py
```

Enter the target URL when prompted:

```text
Enter URL: http://example.com/page?id=
```

The scanner will test multiple payloads and display the results.

---

## Expected Output

### Vulnerable Target

```text
[!] Possible SQL Injection detected!

[+] Target appears VULNERABLE!
```

### Non-Vulnerable Target

```text
[-] No obvious vulnerability detected

[-] Target does NOT appear vulnerable
```

---

## Educational Objective

The primary objective of this project is to understand:

* Web application security fundamentals.
* SQL Injection attack vectors.
* Automated vulnerability assessment techniques.
* HTTP request and response analysis.
* Secure coding and input validation practices.

---

## Disclaimer

This project is developed strictly for educational and authorized security testing purposes. Users must obtain proper permission before testing any web application. Unauthorized security testing may violate legal and ethical guidelines.

---

## Author

**M Hafiza**
**Intern ID:** CITS1108
**Project:** SQL Injection Vulnerability Scanner
**Duration:** 8 Weeks
