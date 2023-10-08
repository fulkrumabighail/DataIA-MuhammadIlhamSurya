def count_word_occurrences(DATA, QUERIES):
    # Initialize an empty dictionary to store word counts
    word_counts = {}

    # Convert DATA list to a string
    data_string = ' '.join(DATA)

    # Iterate through each word in QUERIES
    for word in QUERIES:
        # Count occurrences of the word in DATA
        count = data_string.count(word)
        word_counts[word] = count

    return word_counts

# Example usage:
DATA = ["saya", "suka", "makan", "sate", "sate", "ayam"]
QUERIES = ["sate", "saya", "nasi", "makan"]

result = count_word_occurrences(DATA, QUERIES)
print(result)