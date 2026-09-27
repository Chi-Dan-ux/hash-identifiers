# test.py

# We need to borrow the identify_hash function from hash.py
from hash import identify_hash

# Here are some hashes where we ALREADY KNOW the right answer
# (these are all the hash of an empty string "", found from public references)
known_hashes = {
    "d41d8cd98f00b204e9800998ecf8427e": "MD5",
    "da39a3ee5e6b4b0d3255bfef95601890afd80709": "SHA-1",
    "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855": "SHA-256",
}

# Let's check each one
for hash_value, correct_answer in known_hashes.items():
    guesses = identify_hash(hash_value)

    if correct_answer in guesses:
        print(f"PASS: {hash_value} correctly matched with {correct_answer}")
    else:
        print(f"FAIL: {hash_value} — expected {correct_answer}, got {guesses}")