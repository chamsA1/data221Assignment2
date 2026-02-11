# Dictionary to group lines by their normalized form
normalized_groups = {}

with open("sample-file.txt", "r") as file:
    for line_number, line_text in enumerate(file, start=1):

        original_line = line_text.rstrip("\n")

        normalized_line = ""
        for character in original_line.lower():
            if character.isalnum():          # keeps letters + digits only
                normalized_line += character

        # Skip lines that become empty after normalization
        if normalized_line == "":
            continue

        # Add the line to its group
        if normalized_line not in normalized_groups:
            normalized_groups[normalized_line] = []

        normalized_groups[normalized_line].append((line_number, original_line))


# Collect only the groups that have 2+ lines (meaning duplicates)
duplicate_sets = []
for group_lines in normalized_groups.values():
    if len(group_lines) >= 2:
        duplicate_sets.append(group_lines)

print("Number of near-duplicate sets:", len(duplicate_sets))

# Print the first two duplicate sets found
for set_index in range(min(2, len(duplicate_sets))):
    print("\nSet", set_index + 1, ":")
    for line_number, original_line in duplicate_sets[set_index]:
        print(str(line_number) + ":", original_line)
