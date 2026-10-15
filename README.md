# CodeAlpha Secure Coding Review

## Overview
This project demonstrates a security review of a Python Flask
application. I identified common vulnerabilities, applied fixes,
and compared Bandit results before and after remediation.

## Vulnerabilities Reviewed
- SQL Injection
- Cross-Site Scripting (XSS)
- Command Injection
- Flask Debug Mode

## Tools Used
- Python
- Flask
- SQLite
- Bandit
- Kali Linux

## Security Improvements
- Used parameterized SQL queries.
- Escaped user input before displaying it in HTML.
- Replaced shell-based command execution with subprocess.run()
  using a list of arguments.
- Validated IP addresses and added a timeout.
- Disabled Flask debug mode.

## Testing
The login tests confirmed that the sample account could log in
and a SQL injection test string was rejected.
Additional testing checked HTML escaping and invalid IP input.

## Bandit Results
Initial scan: 4 findings.
After fixes: 3 low-severity findings.

The remaining findings require manual review. A clean scan
does not guarantee that an application is secure.

## Run Locally
Install Flask with:

pip install Flask

Start the application with:

python3 app.py

Open http://127.0.0.1:5000 in your browser.

## Disclaimer
This is a learning project, not a production-ready application.
