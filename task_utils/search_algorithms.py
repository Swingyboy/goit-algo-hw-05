from typing import Dict, List


def booyer_moore_search(text: str, pattern: str) -> int:
    # Preprocessing
    skip: Dict[str, int] = {}
    for i in range(len(pattern)):
        skip[pattern[i]] = len(pattern) - i - 1

    # Searching
    i = len(pattern) - 1
    while i < len(text):
        j = len(pattern) - 1
        while text[i] == pattern[j]:
            if j == 0:
                return i
            i -= 1
            j -= 1
        i += skip.get(text[i], len(pattern))
    return -1


def kmp_search(text: str, pattern: str) -> int:
    # Preprocessing
    prefix: List[int] = [0] * len(pattern)
    j: int = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = prefix[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        prefix[i] = j

    # Searching
    j = 0
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = prefix[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == len(pattern):
            return i - len(pattern) + 1
    return -1


def rabin_karp_search(text: str, pattern: str) -> int:
    # Preprocessing
    d: int = 256
    q: int = 101
    n: int = len(text)
    m: int = len(pattern)
    h: int = pow(d, m - 1) % q
    p: int = 0
    t: int = 0
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    # Searching
    for s in range(n - m + 1):
        if p == t:
            match = True
            for i in range(m):
                if pattern[i] != text[s + i]:
                    match = False
                    break
            if match:
                return s
        if s < n - m:
            t = (d * (t - ord(text[s]) * h) + ord(text[s + m])) % q
            if t < 0:
                t += q
    return -1
