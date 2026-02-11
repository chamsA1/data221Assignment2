# Function to find lines containing a keyword (case-insensitive)
def find_lines_containing(filename, keyword):

    matching_lines = []

    # Open file and read line by line
    with open(filename, "r") as file:

        for line_number, line_text in enumerate(file, start=1):

            # Convert both line and keyword to lowercase
            if keyword.lower() in line_text.lower():

                # Remove newline from end of line
                clean_line = line_text.strip()

                # Save line number and text
                matching_lines.append((line_number, clean_line))


    return matching_lines

file_name = "sample-file.txt"
search_word = "lorem"

results = find_lines_containing(file_name, search_word)


print("Number of matching lines:", len(results))


# Print first 3 matches
print("\nFirst 3 matching lines:")

for i in range(min(3, len(results))):

    line_number = results[i][0]
    line_text = results[i][1]

    print(line_number, ":", line_text)
