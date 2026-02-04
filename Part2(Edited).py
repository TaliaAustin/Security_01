"""
CSC 348/648: Assignment 1 Part 2
Author: Talia Austin
Date: January 29, 2026

AI Assistance: Claude (Anthropic) was used to help debug code, 
explain concepts, and provide guidance on implementation approaches.
And GitHub Copilot was used to suggest code snippets.
"""

def frequency_analysis(text):
    """
   Analyze letter frequencies in text (uppercase letters and space only).
    
    Args:
        text: Input string
        
    Returns:
        Dictionary with keys 'A'-'Z' and ' ', values are frequencies (0.0-1.0)
   """

    # Intialize dictionary letters without spaces

    dictionary_freq = {}
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ ":
        dictionary_freq[letter] = 0


    # ensure text uppercase and count letters
    text_upper = text.upper()
    valid_chars = [ char for char in text_upper if char in dictionary_freq ]
    total_chars = len(valid_chars)

    # count frequencies
    if total_chars == 0:
        return dictionary_freq  # avoid division by zero
    
    for char in valid_chars:
        dictionary_freq[char] += 1

    # convert counts to frequencies
    for char in dictionary_freq:
        dictionary_freq[char] = dictionary_freq[char] / total_chars
    
    return dictionary_freq

# test the function
test_text = "AB CD"
result = frequency_analysis(test_text)
print(result)  
# Expected output: {'A': 0.2, 'B': 0.2, 'C': 0.2, 'D': 0.2, ... , 'Z': 0.0}

def cross_correlation(freq1, freq2):
    """
    What is the cross-correlation of Set 1 and Set 2? 0.003098
    What is the cross-correlation of Set 1 and Set 3? 0.0014600000000000001
    """
    correlation = 0.0

    common_letters = set(freq1.keys()) & (set(freq2.keys()))

    for key in common_letters:
        correlation += freq1[key] * freq2[key]
    return correlation
    
set1 = {'A': 0.012, 'B': 0.003, 'C': 0.01, 'D': 0.1, 'E': 0.02, 'F': 0.001}
set2 = {'A': 0.001, 'B': 0.012, 'C': 0.003, 'D': 0.01, 'E': 0.1, 'F': 0.02}
set3 = {'A': 0.01, 'B': 0.02, 'C': 0.001, 'D': 0.012, 'E': 0.003, 'F': 0.01}

print(f"Cross-correlation Set1& set2: {cross_correlation(set1, set2)}")  # Expected output: small float value
print(f"Cross-correlation Set1& set3: {cross_correlation(set1, set3)}")  # Expected output: small float value


def get_caesar_shift(enc_message, expected_dist):
    """
        Determine the Caesar cipher shift used to encrypt a message based on frequency analysis.
        
        Args:
            enc_message: The encrypted message string.
            expected_dist: A dictionary with expected letter frequencies.
            
        Returns:
             The most likely shift value (integer).
    """
    
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ " 

    freq_table = frequency_analysis(enc_message)


    set_1 = [freq_table[alphabet[i]] for i in range(27)]
    set_2 = [expected_dist[alphabet[i]] for i in range(27)]


    best_shift = 0
    best_score = float('-inf')

    for s in range(27):
        score = 0.0
        for i in range(27):
            score += set_1[i] * set_2[(i - s) % 27]

        print(f"Shift {s}: score = {score:.6f}") 

        if score > best_score:
            best_score = score
            best_shift = s

    return best_shift

    
    


def get_vigenere_keyword(enc_message, key_length, expected_dist):
    """
    Determine the Vigenere cipher keyword used to encrypt a message based on frequency analysis.
    
    Args:
        enc_message: The encrypted message string.
        keyword_length: The length of the keyword.
        expected_dist: A dictionary with expected letter frequencies.
        
    Returns:
        The most likely keyword (string).
    """
    
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

    cols = ["" for _ in range(key_length)]

    t = 0

    for ch in enc_message:
        if ch in alphabet:
            j = t % key_length
            cols[j] += ch
            t += 1

    keyword = ""
    for j in range(key_length):
        s = get_caesar_shift(cols[j], expected_dist)
        keyword += alphabet[s]

    return keyword