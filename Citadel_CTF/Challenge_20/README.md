# BRATCHA

## Description

A clear chime rolls through the chamber and a new crest ignites on your badge – a quiet promotion. The outer ring is behind you. From here, the Citadel opens its inner systems, and the locks grow heavier because the keys are worth more. Your answers now carry more weight – and earn more in return. The citadel welcomes you to the inner climb.

Near the gate to the next floor you come across a CAPTCHA verification test, but it has been covered by scratches on the decaying wall and misleading letters stopping you from finding the correct key, all to prove you’re human.

## Solution
Looking at the QR image, every position had 2 overlapping letters which i figured out to be
```
sgxnxBnS
cqyhyDhZ
```

I wrote a simple script to bruteforce all 256 possible permutations
```python
import subprocess

codes = [
    "cqxnvDnZ","cqxnvDnS","cqxnvDhZ","cqxnvDhS","cqxnvBnZ","cqxnvBnS","cqxnvBhZ","cqxnvBhS",
    "cqxnxDnZ","cqxnxDnS","cqxnxDhZ","cqxnxDhS","cqxnxBnZ","cqxnxBnS","cqxnxBhZ","cqxnxBhS",
    "cqxhvDnZ","cqxhvDnS","cqxhvDhZ","cqxhvDhS","cqxhvBnZ","cqxhvBnS","cqxhvBhZ","cqxhvBhS",
    "cqxhxDnZ","cqxhxDnS","cqxhxDhZ","cqxhxDhS","cqxhxBnZ","cqxhxBnS","cqxhxBhZ","cqxhxBhS",
    "cqynvDnZ","cqynvDnS","cqynvDhZ","cqynvDhS","cqynvBnZ","cqynvBnS","cqynvBhZ","cqynvBhS",
    "cqynxDnZ","cqynxDnS","cqynxDhZ","cqynxDhS","cqynxBnZ","cqynxBnS","cqynxBhZ","cqynxBhS",
    "cqyhvDnZ","cqyhvDnS","cqyhvDhZ","cqyhvDhS","cqyhvBnZ","cqyhvBnS","cqyhvBhZ","cqyhvBhS",
    "cqyhxDnZ","cqyhxDnS","cqyhxDhZ","cqyhxDhS","cqyhxBnZ","cqyhxBnS","cqyhxBhZ","cqyhxBhS",
    "cgxnvDnZ","cgxnvDnS","cgxnvDhZ","cgxnvDhS","cgxnvBnZ","cgxnvBnS","cgxnvBhZ","cgxnvBhS",
    "cgxnxDnZ","cgxnxDnS","cgxnxDhZ","cgxnxDhS","cgxnxBnZ","cgxnxBnS","cgxnxBhZ","cgxnxBhS",
    "cgxhvDnZ","cgxhvDnS","cgxhvDhZ","cgxhvDhS","cgxhvBnZ","cgxhvBnS","cgxhvBhZ","cgxhvBhS",
    "cgxhxDnZ","cgxhxDnS","cgxhxDhZ","cgxhxDhS","cgxhxBnZ","cgxhxBnS","cgxhxBhZ","cgxhxBhS",
    "cgynvDnZ","cgynvDnS","cgynvDhZ","cgynvDhS","cgynvBnZ","cgynvBnS","cgynvBhZ","cgynvBhS",
    "cgynxDnZ","cgynxDnS","cgynxDhZ","cgynxDhS","cgynxBnZ","cgynxBnS","cgynxBhZ","cgynxBhS",
    "cgyhvDnZ","cgyhvDnS","cgyhvDhZ","cgyhvDhS","cgyhvBnZ","cgyhvBnS","cgyhvBhZ","cgyhvBhS",
    "cgyhxDnZ","cgyhxDnS","cgyhxDhZ","cgyhxDhS","cgyhxBnZ","cgyhxBnS","cgyhxBhZ","cgyhxBhS",
    "sqxnvDnZ","sqxnvDnS","sqxnvDhZ","sqxnvDhS","sqxnvBnZ","sqxnvBnS","sqxnvBhZ","sqxnvBhS",
    "sqxnxDnZ","sqxnxDnS","sqxnxDhZ","sqxnxDhS","sqxnxBnZ","sqxnxBnS","sqxnxBhZ","sqxnxBhS",
    "sqxhvDnZ","sqxhvDnS","sqxhvDhZ","sqxhvDhS","sqxhvBnZ","sqxhvBnS","sqxhvBhZ","sqxhvBhS",
    "sqxhxDnZ","sqxhxDnS","sqxhxDhZ","sqxhxDhS","sqxhxBnZ","sqxhxBnS","sqxhxBhZ","sqxhxBhS",
    "sqynvDnZ","sqynvDnS","sqynvDhZ","sqynvDhS","sqynvBnZ","sqynvBnS","sqynvBhZ","sqynvBhS",
    "sqynxDnZ","sqynxDnS","sqynxDhZ","sqynxDhS","sqynxBnZ","sqynxBnS","sqynxBhZ","sqynxBhS",
    "sqyhvDnZ","sqyhvDnS","sqyhvDhZ","sqyhvDhS","sqyhvBnZ","sqyhvBnS","sqyhvBhZ","sqyhvBhS",
    "sqyhxDnZ","sqyhxDnS","sqyhxDhZ","sqyhxDhS","sqyhxBnZ","sqyhxBnS","sqyhxBhZ","sqyhxBhS",
    "sgxnvDnZ","sgxnvDnS","sgxnvDhZ","sgxnvDhS","sgxnvBnZ","sgxnvBnS","sgxnvBhZ","sgxnvBhS",
    "sgxnxDnZ","sgxnxDnS","sgxnxDhZ","sgxnxDhS","sgxnxBnZ","sgxnxBnS","sgxnxBhZ","sgxnxBhS",
    "sgxhvDnZ","sgxhvDnS","sgxhvDhZ","sgxhvDhS","sgxhvBnZ","sgxhvBnS","sgxhvBhZ","sgxhvBhS",
    "sgxhxDnZ","sgxhxDnS","sgxhxDhZ","sgxhxDhS","sgxhxBnZ","sgxhxBnS","sgxhxBhZ","sgxhxBhS",
    "sgynvDnZ","sgynvDnS","sgynvDhZ","sgynvDhS","sgynvBnZ","sgynvBnS","sgynvBhZ","sgynvBhS",
    "sgynxDnZ","sgynxDnS","sgynxDhZ","sgynxDhS","sgynxBnZ","sgynxBnS","sgynxBhZ","sgynxBhS",
    "sgyhvDnZ","sgyhvDnS","sgyhvDhZ","sgyhvDhS","sgyhvBnZ","sgyhvBnS","sgyhvBhZ","sgyhvBhS",
    "sgyhxDnZ","sgyhxDnS","sgyhxDhZ","sgyhxDhS","sgyhxBnZ","sgyhxBnS","sgyhxBhZ","sgyhxBhS"
]

for code in codes:
    url = f"https://pastebin.com/{code}"
    result = subprocess.run(["curl", "-s", "-L", url], stdout=subprocess.PIPE)
    if '404 Not Found' not in result.stdout.decode() and 'This page is no longer available' not in result.stdout.decode():
        print(f"Working Link: {url}")
```

I got the working url as `https://pastebin.com/sqxnxBhZ`

## Flag
`citadel{1m_3v3rywh3r3_1m_s0_jul1a}`
