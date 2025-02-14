Scripts used for SHA-256 hashed password cracking in a CTF Challenge.

hash will take known passwords, their hashed values, and their salt to figure out the salt pattern.

pass will test common passwords against given hash values and salts using the SHA-256(salt+password) pattern to reverse the hash and find the original password.

