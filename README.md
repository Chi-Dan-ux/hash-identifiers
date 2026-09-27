# Hash Identifier

A beginner Python project that identifies the likely type of a cryptographic hash based on its length and character set.

## What it does

Given a hash string, the tool guesses which hashing algorithm was likely used to generate it (e.g. MD5, SHA-1, SHA-256, bcrypt). It does **not** decode or crack the hash — hashes are one-way and cannot be reversed. It only recognizes the "shape" of common hash types.

## Supported hash types

| Algorithm     | Length (hex chars) |
|---------------|---------------------|
| CRC32         | 8                   |
| MD5 / NTLM / MD4 | 32               |
| SHA-1 / RIPEMD-160 | 40              |
| SHA-224       | 56                  |
| SHA-256 / SHA3-256 | 64              |
| SHA-384       | 96                  |
| SHA-512 / SHA3-512 | 128             |
| bcrypt        | starts with `$2a$`, `$2b$`, or `$2y$` |

Some lengths are ambiguous (e.g. MD5 and NTLM are both 32 characters), so the tool lists **all** possible matches rather than guessing just one.

## Usage

```bash
python hash.py
```

You'll be prompted to enter a hash, and the tool will print its length and all possible matching algorithm types.

### Example

```
Enter a hash to identify: d41d8cd98f00b204e9800998ecf8427e

Hash: d41d8cd98f00b204e9800998ecf8427e
Length: 32 characters
Possible type(s):
  - MD5
  - NTLM
  - MD4
```

## Running tests

`test.py` checks the identifier against hashes with known, verified answers:

```bash
python test.py
```

## Why this project

Built as a beginner cybersecurity project to practice recognizing hash formats — a useful skill when analyzing leaked credential dumps, CTF challenges, or pentest output.

## Disclaimer

This tool identifies *possible* hash types based on pattern-matching only. It cannot verify a guess with certainty, and it does not crack, decode, or reverse hashes in any way.
