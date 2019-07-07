# Useful-Python-Snippets
![python](https://img.shields.io/pypi/pyversions/Django.svg)
![size](https://img.shields.io/github/repo-size/ak-wa/Useful-Python-Snippets.svg)
![lastcommit](https://img.shields.io/github/last-commit/ak-wa/Useful-Python-Snippets.svg)
![follow](https://img.shields.io/github/followers/ak-wa.svg?label=Follow&style=social)

Here I put my Python snippets that may be useful for one or the other purpose.

### check_sqli.py
* Checks for basic SQL Injection on a list of targets
* Adds "'"(part of SQL Syntax) to the end of url & checks response html for SQL errors
* Usage in code: `check_sqli("example_target_list.txt")`

### tor_check.py

* Tries to route the script through tor on socks5://127.0.0.1:9150 ; prints your remote ip address.

### haveibeenpwned.py

* Checks an email for database leaks on https://haveibeenpwned.com
* Usage in code: `mail_check("example@example.com")`

### robots_check.py

* Checks a website.com/robots.txt for entries & prints them out
* Usage in code: `robots_check("https://www.example.com")`
