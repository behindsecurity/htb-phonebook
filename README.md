# htb-phonebook
A simple python script to pwn [phonebook challenge](https://app.hackthebox.com/challenges/Phonebook) from HackTheBox.

## Quick Summary
Allowing wildcards like * in passwords can introduce vulnerabilities. If a system interprets a wildcard as matching any sequence of characters, attackers could exploit this feature to guess passwords through brute force attacks, one character at a time. This is not common in real life, though.

## How It Works
Imagine a login system where, during authentication, the system checks if the entered password matches the stored password for a user. If the system treats certain wildcard characters in a special way, where a * can match any string of characters, an attacker can exploit this feature to guess passwords. For example:

1. If an attacker enters h* as a password, and the system validates it as a match for any user whose password starts with "h", then the attacker knows that "h" is a valid starting character for the password.
2. By systematically trying different characters followed by *, an attacker can gradually determine the entire password, one character at a time.

## Run
For this to work, you must change the initial variables to match your environment.

```python
URL = "http://94.237.62.149:56117" # Replace this with your challenge address
MAX_WORKERS = 10  # Adjust based on your system's capability
```

After that, just run it: `python3 phonebook.py`
