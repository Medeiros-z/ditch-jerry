import hashlib

def test_hashing(password, salt, expected_hash):
    methods = {
        "salt+password": salt + password,
        "password+salt": password + salt,
        "salt:password": salt + ":" + password,
        "password:salt": password + ":" + salt,
        "salt.upper() + password": salt.upper() + password,
        "salt.lower() + password": salt.lower() + password,
        "base64(salt) + password": salt.encode().hex() + password,
    }
    
    for name, method in methods.items():
        hashed = hashlib.sha256(method.encode()).hexdigest()
        if hashed == expected_hash:
            print(f"Match found for {name}: {method}")
            return name

    print("No matching hash method found for user.")
    return None

# Given credentials
# password, salt, hashed password
test_hashing("123", "ZiE7MWuGSEw", "e477b08ada4c696de921e967aeeca7725f8a6daddf9cd8eaf3d669dfa581c4d7")
test_hashing("1234", "ul8IWnsezxo", "07f6da5fa8577b7357f9565587d3e122e3edf909b5fb63e639e43aa649046eb9")