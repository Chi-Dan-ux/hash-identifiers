# hash.py

def identify_hash(hash_string):
    # Clean up whitespace from copy-pasting
    hash_string = hash_string.strip()

    length = len(hash_string)

    # Check if valid hex (0-9, a-f, A-F)
    is_hex = all(c in "0123456789abcdefABCDEF" for c in hash_string)

    if not is_hex:
        # Not hex — might still be another format, like bcrypt
        if hash_string.startswith(("$2a$", "$2b$", "$2y$")):
            return ["bcrypt"]
        return ["Unknown — contains non-hex characters"]

    # Map lengths to possible hash types (a list, since matches can be ambiguous)
    possible_matches = {
        8: ["CRC32"],
        32: ["MD5", "NTLM", "MD4"],
        40: ["SHA-1", "RIPEMD-160"],
        56: ["SHA-224"],
        64: ["SHA-256", "SHA3-256"],
        96: ["SHA-384"],
        128: ["SHA-512", "SHA3-512"],
    }

    return possible_matches.get(length, ["Unknown hash type"])


def format_results(hash_string, matches):
    # Build a nice readable output block
    output = f"\nHash: {hash_string}\n"
    output += f"Length: {len(hash_string)} characters\n"
    output += "Possible type(s):\n"
    for match in matches:
        output += f"  - {match}\n"
    return output


if __name__ == "__main__":
    user_input = input("Enter a hash to identify: ")
    matches = identify_hash(user_input)
    print(format_results(user_input, matches))