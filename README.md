# 🔐 Password Strength & Breach Checker

A simple Python tool that helps you test if your password is **strong** and if it has ever been exposed in a **data breach**.

This project checks password quality using basic security rules (inspired by OWASP) and uses the [Have I Been Pwned](https://haveibeenpwned.com/) API to check if your password has been leaked — all while keeping your password private.

---

## 🚀 Features

- ✅ Checks password length (minimum 8 characters recommended)
- ✅ Verifies character variety (uppercase, lowercase, digits, special characters)
- ✅ Detects common weak passwords (like `123456`, `password`, etc.)
- ✅ Uses SHA-1 and **k-Anonymity** to securely check breach status
- ✅ Gives clear, helpful feedback to improve password strength

---

## 🛠 Requirements

- Python 3.6 or higher  
- `requests` library

To install dependencies:

```bash
pip install requests
```
## 🧪 How to Use
Run the script from your terminal or Python IDLE:
```bash
python password_checker.py
```
You’ll be asked to enter a password. The tool will then:

- Evaluate its strength

- Check if it appears in known breaches

 ## 🔐 How is my password protected?
- Your full password is never sent online.
- Only the first 5 characters of its SHA-1 hash are sent to the HIBP API.
- This method (called k-Anonymity) ensures your privacy while still checking millions of leaked passwords.

## 📁 Project Files
- `password_checker.py` – main script

- `requirements.txt` – list of dependencies

## 📚 Why This Tool?
- I created this tool to help anyone easily:

- Understand what makes a password strong

- Check if a password has been compromised

- Learn how to build safer digital habits

- You can use it locally, teach with it, or extend it for bigger projects.

##  💬 Questions?
If you need help or have ideas for improvement, feel free to open an issue or reach out!





