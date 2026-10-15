# Secure Coding Review

## 1. Project Overview

This project demonstrates a manual and automated security review of a deliberately vulnerable Python web application built with Flask. Bandit was used to identify potential security issues, and the source code was reviewed manually to identify additional risks.

The goal was to understand common vulnerabilities, implement appropriate fixes, and compare static analysis results before and after remediation.

## 2. Tools Used

- Python
- Flask
- SQLite
- Bandit
- Kali Linux

## 3. Vulnerabilities Identified

### SQL Injection

**Location:** `/login` route

**Risk:** The original code joined user-supplied usernames and passwords directly into an SQL query. An attacker could manipulate the query to bypass intended database checks.

**Fix:** Replaced string concatenation with a parameterized SQLite query using placeholders.

### Cross-Site Scripting (XSS)

**Location:** `/hello` route

**Risk:** The original code inserted user input directly into an HTML response. A browser could interpret injected HTML as markup rather than plain text.

**Fix:** Used `markupsafe.escape()` to escape the supplied name before inserting it into the response.

### Command Injection

**Location:** `/ping` route

**Risk:** The original code passed user input into a shell command using `subprocess.getoutput()`. This could allow unintended command execution.

**Fix:** Replaced the shell-based call with `subprocess.run()` using a list of arguments, added a timeout, and validated the input as an IP address.

### Flask Debug Mode

**Location:** Application startup

**Risk:** Enabling debug mode in a production deployment can expose sensitive details and an interactive debugger.

**Fix:** Set `debug=False`.

## 4. Static Analysis Results

Bandit was run before and after the code changes.

| Finding severity | Initial scan | After fixes |
|---|---:|---:|
| High | 2 | 0 |
| Medium | 1 | 0 |
| Low | 1 | 3 |
| Total findings | 4 | 3 |

The initial scan identified potentially unsafe SQL construction, shell-based command execution, and Flask debug mode. The updated scan no longer reported those original findings.

The remaining low-severity findings relate to the use of `subprocess`, the partial executable path for `ping`, and the subprocess call itself. These findings require contextual review and should not automatically be treated as confirmed exploitable vulnerabilities.

## 5. Limitations

Bandit is a static analysis tool. It cannot detect every vulnerability, and a clean scan does not prove that an application is secure.

Manual review remains necessary. This review also identified the XSS risk, which was not reported by the initial Bandit scan.

The updated application still requires functional testing and further review before being considered suitable for production.

## 6. Conclusion

This project provided practical experience in reviewing Python code, understanding common web application vulnerabilities, applying basic remediation techniques, and using Bandit to compare security findings before and after changes.

The exercise demonstrated that automated scanning is useful, but it should be combined with manual code review and testing.
