from collections import Counter#Counter is a dictionary that automatically counts how many times each item appears in a list.

# Open and read the text file
with open("sample-file.txt", "r", encoding="utf-8") as file:
    file_text = file.read()

# Convert all text to lowercase
file_text = file_text.lower()

# Split text into words using spaces
raw_words = file_text.split()

cleaned_words = []

# Clean and filter each word
for word in raw_words:

    # Remove punctuation from start and end
    cleaned_word = word.strip(".,!?;:'\"()[]{}")

    # Count how many letters are in the word
    letter_count = 0
    for character in cleaned_word:
        if character.isalpha():
            letter_count += 1

    # Keep only words with at least 2 letters
    if letter_count >= 2:
        cleaned_words.append(cleaned_word)

# Count how many times each word appears
word_frequencies = Counter(cleaned_words)

# Print the 10 most common words
print("Top 10 words:")

for word, count in word_frequencies.most_common(10):
    print(word, "->", count)
