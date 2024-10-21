import os
import socket
from collections import Counter
import re

def clean_text(text):
    # Split on whitespace and handle contractions
    words = re.findall(r"\b\w+\b", text.lower())  # Extract words, handling contractions
    return words

def count_words(filename):
    with open(filename, 'r') as file:
        text = file.read()
        words = clean_text(text)
        word_count = len(words)
        word_freq = Counter(words)
    return word_count, word_freq

def get_top_words(word_freq, top_n=3):
    return word_freq.most_common(top_n)

# Paths to the text files
file1 = '/home/data/IF.txt'
file2 = '/home/data/AlwaysRememberUsThisWay.txt'

# Count words in both files
word_count1, word_freq1 = count_words(file1)
word_count2, word_freq2 = count_words(file2)

# Grand total of words
grand_total_words = word_count1 + word_count2

# Top 3 words from each file
top_words_file1 = get_top_words(word_freq1)
top_words_file2 = get_top_words(word_freq2)

# Get the container's IP address
ip_address = socket.gethostbyname(socket.gethostname())

# Prepare the results
result = (
    f"Word count in IF.txt: {word_count1}\n"
    f"Word count in AlwaysRememberUsThisWay.txt: {word_count2}\n"
    f"Grand total word count: {grand_total_words}\n\n"
    f"Top 3 words in IF.txt: {top_words_file1}\n"
    f"Top 3 words in AlwaysRememberUsThisWay.txt: {top_words_file2}\n\n"
    f"Container IP Address: {ip_address}\n"
)

# Output file path
output_path = '/home/data/output/result.txt'

# Write results to file
os.makedirs('/home/data/output', exist_ok=True)
with open(output_path, 'w') as file:
    file.write(result)

# Print result to console
print(result)