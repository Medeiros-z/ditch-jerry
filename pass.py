import hashlib

# Load users, salts, and hashes
user_data = {
    "zack":    ("ul8IWnsezxo", "07f6da5fa8577b7357f9565587d3e122e3edf909b5fb63e639e43aa649046eb9"),
    "zacka":   ("ZiE7MWuGSEw", "e477b08ada4c696de921e967aeeca7725f8a6daddf9cd8eaf3d669dfa581c4d7"),
    "jerry":   ("QS_edf8TSik", "5a53ed423b9ebb2b30db70e167d3a60e468c178d70a05fd8beba6ff12abb90ad"),
    # Add more users if available
}

# Load a wordlist of common passwords
password_list = open("rockyou.txt", "r", encoding="latin-1").read().splitlines()


def crack_password():
    for user, (salt, expected_hash) in user_data.items():
        for password in password_list:
            test_hash = hashlib.sha256((salt + password).encode()).hexdigest()
            if test_hash == expected_hash:
                print(f"[+] CRACKED! User: {user}, Password: {password}")
                break
        else:
            print(f"[-] No match found for {user}")

# Run brute-force attack
crack_password()
