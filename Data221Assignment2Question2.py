# Open and read the text file
with open("sample-file.txt", "r") as file:
    file_text = file.read()

# Convert text to lowercase
file_text = file_text.lower()

# Splits text into words
raw_words = file_text.split()

cleaned_words = []

# cleans the words
for word in raw_words:

    # Remove punctuation
    cleaned_word = word.strip(".,!?;:'\"()[]{}")

    # Count letters in the word
    letter_count = 0
    for character in cleaned_word:
        if character.isalpha():
            letter_count += 1

    # Keep only words with at least 2 letters
    if letter_count >= 2:
        cleaned_words.append(cleaned_word)


# Dictionary to store bigram frequencies
bigram_frequencies = {}

# Build and count bigrams
for i in range(len(cleaned_words) - 1):

    # Create a pair of consecutive words
    first_word = cleaned_words[i]
    second_word = cleaned_words[i + 1]

    bigram = first_word + " " + second_word

    # Count the bigram
    if bigram in bigram_frequencies:
        bigram_frequencies[bigram] += 1
    else:
        bigram_frequencies[bigram] = 1

# Sort bigrams by frequency (highest first)
sorted_bigrams = sorted(
    bigram_frequencies.items(),
    key=lambda item: item[1],
    reverse=True
)


# Print top 5 bigrams
print("Top 5 bigrams:")

for i in range(5):
    bigram = sorted_bigrams[i][0]
    count = sorted_bigrams[i][1]

    print(bigram, "->", count)
