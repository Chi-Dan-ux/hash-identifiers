# hash.py

import sys

def identify_hash(hash_string):
    hash_string = hash_string.strip()

    prefix_matches = {
        "$2a$": "bcrypt",
        "$2b$": "bcrypt",
        "$2y$": "bcrypt",
        "$1$": "MD5-crypt (Linux)",
        "$5$": "SHA-256-crypt (Linux)",
        "$6$": "SHA-512-crypt (Linux)",
        "$argon2i$": "Argon2i",
        "$argon2id$": "Argon2id",
    }

    for prefix, hash_type in prefix_matches.items():
        if hash_string.startswith(prefix):
            return [hash_type]

    length = len(hash_string)
    is_hex = all(c in "0123456789abcdefABCDEF" for c in hash_string)

    if not is_hex:
        return ["Unknown — contains non-hex characters and no known prefix"]

    possible_matches = {
        8: ["CRC32"],
        32: ["MD5", "NTLM", "MD4"],
        40: ["SHA-1", "RIPEMD-160"],
        48: ["Tiger-192"],
        56: ["SHA-224"],
        64: ["SHA-256", "SHA3-256", "Whirlpool (partial)"],
        96: ["SHA-384"],
        128: ["SHA-512", "SHA3-512", "Whirlpool"],
    }

    return possible_matches.get(length, ["Unknown hash type"])


def format_results(hash_string, matches):
    output = f"\nHash: {hash_string}\n"
    output += f"Length: {len(hash_string)} characters\n"
    output += "Possible type(s):\n"
    for match in matches:
        output += f"  - {match}\n"
    return output


if __name__ == "__main__":
    # Did the user hand us a hash already, like a note passed to us?
    if len(sys.argv) > 1:
        user_input = sys.argv[1]
    else:
        # Nope — ask for it the old way
        user_input = input("Enter a hash to identify: ")

    matches = identify_hash(user_input)
    print(format_results(user_input, matches))