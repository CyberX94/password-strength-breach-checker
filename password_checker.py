import hashlib
import requests
import re

def evaluate_password_strength(password):
    feedback = []
    length = len(password)
    
    # Rule 1: Check length
    if length < 8:
        feedback.append("Password is too short. Use at least 12 characters.")
        
    # Rule 2: Check for uppercase letters
    if not re.search(r'[A-Z]', password):
        feedback.append("Add uppercase letters (A-Z).")
    
    # Rule 3: Check for lowercase letters
    if not re.search(r'[a-z]', password):
        feedback.append("Add lowercase letters (a-z).")
    
    # Rule 4: Check for digits
    if not re.search(r'\d', password):
        feedback.append("Include numbers (0-9).")
    
    # Rule 5: Check for special characters
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        feedback.append("Include special characters like !@#$%^&*.")
    
    # Rule 6: Avoid common passwords or patterns (basic dictionary check)
    common_words = ['password', '123456', 'qwerty', 'abc123', 'letmein']
    for word in common_words:
        if word in password.lower():
            feedback.append(f"Avoid common words or patterns like '{word}'.")
            break
    
    if len(feedback) == 0:
        feedback.append("Strong password!")
    
    return feedback

def get_password_hash_sha1(password):
    # Hash the password using SHA-1 (required for HIBP API)
    sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    return sha1

def check_pwned_password(password):
    # Use k-Anonymity: send first 5 chars of SHA-1 hash to HIBP API
    sha1 = get_password_hash_sha1(password)
    prefix = sha1[:5]
    suffix = sha1[5:]
    
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print("Error querying Have I Been Pwned API.")
            return None
        
        # Parse the response and look for matching suffix
        hashes = (line.split(':') for line in response.text.splitlines())
        for hash_suffix, count in hashes:
            if hash_suffix == suffix:
                return int(count)
        return 0
    except requests.RequestException:
        print("Network error while contacting Have I Been Pwned API.")
        return None

def main():
    print("Password Strength & Breach Detection Tool (OWASP & HIBP)")
    password = input("Enter a password to test: ")
    
    print("\nEvaluating password strength...")
    feedback = evaluate_password_strength(password)
    for f in feedback:
        print(f"- {f}")
    
    print("\nChecking password against known data breaches...")
    pwned_count = check_pwned_password(password)
    if pwned_count is None:
        print("Could not check password breach status.")
    elif pwned_count == 0:
        print("Good news — this password was NOT found in known breaches.")
    else:
        print(f"Warning! This password has appeared {pwned_count} times in data breaches.")
        print("Consider changing it immediately.")
        
if __name__ == "__main__":
    main()
