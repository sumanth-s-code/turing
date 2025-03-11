import re
from collections import Counter

def are_anagrams(str1: str, str2: str) -> bool:
    """
    Check if two strings are anagrams, ignoring spaces, special characters, and considering numbers.
    """
    # Remove non-alphanumeric characters and convert to lowercase
    clean_str1 = re.sub(r'[^a-zA-Z0-9]', '', str1).lower()
    clean_str2 = re.sub(r'[^a-zA-Z0-9]', '', str2).lower()
    
    # Compare character counts using Counter (efficient for large inputs)
    return Counter(clean_str1) == Counter(clean_str2)

# Test cases
test_cases = [
    ("listen", "silent", True),  # Normal case
    ("Hello!!", "oLleh", True),  # Case insensitivity and special characters
    ("Astronomer", "Moon starer", True),  # Space handling
    ("123abc", "cba321", True),  # Numbers handling
    ("123a", "1a23!", True),  # Numbers with special characters
    ("Python", "Java", False),  # Different words
    ("Dormitory", "Dirty Room!", True),  # Common anagram with spaces
    ("The eyes", "They see", True),  # Space handling
    ("aabbcc", "abccba", True),  # Repeated characters
    ("abcd", "abcde", False),  # Extra character
]

# Run tests
for str1, str2, expected in test_cases:
    result = are_anagrams(str1, str2)
    assert result == expected, f"Test failed for: {str1} vs {str2}"
print("All tests passed.")
