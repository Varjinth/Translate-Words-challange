import csv
import time
import sys
import re

# Start the timer
start_time = time.time()

# Read the input text file, find words list text file and dictionary csv file
with open('t8.shakespeare.txt', 'r') as f:
    input_text = f.read()

with open('find_words.txt', 'r') as f:
    find_words = set(f.read().split())

with open('french_dictionary.csv', 'r') as f:
    reader = csv.reader(f)
    dictionary = {row[0]: row[1] for row in reader}

# Find all words that is in the find words list, that has a replacement word in the dictionary
replacements = {}
for word in find_words:
    if word in dictionary:
        replacements[word] = dictionary[word]

# Replace the words in the input text file
output_text = input_text
replace_counts = {}
for word, replacement in replacements.items():
    word_case=word[0].upper() + word[1:]  # Capitalize words eg.Words, Replace
    word_caps=word.upper()                # uppercase words eg. WORDS, REPLACE
    pattern=f'{word}|{word_case}|{word_caps}' # regex pattern to find the words in the textfile
    count = input_text.lower().count(word)
    replace_counts[word] = count
    output_text = re.sub(pattern, replacement, output_text)


# Save the processed file as output
with open('t8.shakespeare.translated.txt', 'w') as f:
    f.write(output_text)

# End the timer
end_time = time.time()

# Calculate the memory usage
memory_usage = sys.getsizeof(input_text) + sys.getsizeof(find_words) + sys.getsizeof(dictionary) + sys.getsizeof(replacements) + sys.getsizeof(output_text) + sys.getsizeof(replace_counts)

# Output the results
# Open a file in write mode
with open('performance.txt', 'w') as f:


    # to display time taken to process and memory usage
    f.write(f'Time taken to process: 0 minutes {end_time - start_time:.2f} seconds\n')
    f.write(f'Memory used: {memory_usage} bytes\n')

with open('frequency.txt', 'w') as f:
    
    # display no. of times a word has been relaced
    f.write('English word,French word,Frequency\n')
    for word, count in replace_counts.items():
        f.write(f'{word},{replacements[word]},{count}\n')
        f.write('\n')

    
