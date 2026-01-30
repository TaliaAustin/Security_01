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
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
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
    best_shift = 0
    best_correlation = -1

    for shift in range(26):
        decrypted = ""

        for char in enc_message:
            if char == ' ':
                decrypted += ' '
            elif char.isalpha():
                decrypted += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                decrypted += char

        freq = frequency_analysis(decrypted)
        
        # Calculate correlation with expected English
        corr = cross_correlation(freq, expected_dist)
        
        # Keep track of best shift
        if corr > best_correlation:
            best_correlation = corr
            best_shift = shift
    
    return best_shift
# Test it
expected_dist = {
    ' ': 0.1828846265, 'E': 0.1026665037, 'T': 0.0751699827, 
    'A': 0.0653216702, 'O': 0.0615957725, 'N': 0.0571201113,
    'I': 0.0566844326, 'S': 0.0531700534, 'R': 0.0498790855,
    'H': 0.0497856396, 'L': 0.0331754796, 'D': 0.0328292310,
    'U': 0.0227579536, 'C': 0.0223367596, 'M': 0.0202656783,
    'F': 0.0198306716, 'W': 0.0170389377, 'G': 0.0162490441,
    'P': 0.0150432428, 'Y': 0.0142766662, 'B': 0.0125888074,
    'V': 0.0079611644, 'K': 0.0056096272, 'X': 0.0014092016,
    'J': 0.0009752181, 'Q': 0.0008367550, 'Z': 0.0005128469
}

# Test with the manual example
test_cipher = "CQN ARPQCB XO NENAH VJW JAN MRVRWRBQNM FQNW CQN ARPQCB XO XWN VJW JAN CQNJCNWNM"
shift = get_caesar_shift(test_cipher, expected_dist)
print(f"Detected shift: {shift}")
# Expected output: Detected shift: 9


def get_vigenere_keyword(enc_message, keyword_length, expected_dist):
    """
    Determine the Vigenere cipher keyword used to encrypt a message based on frequency analysis.
    
    Args:
        enc_message: The encrypted message string.
        keyword_length: The length of the keyword.
        expected_dist: A dictionary with expected letter frequencies.
        
    Returns:
        The most likely keyword (string).
    """
    keyword = ""

    for i in range(keyword_length):
        nth_chars = ""

        for j in range(i, len(enc_message), keyword_length):
            nth_chars += enc_message[j]

        best_shift = get_caesar_shift(nth_chars, expected_dist)
        keyword += chr(best_shift + ord('A'))

    return keyword


        
