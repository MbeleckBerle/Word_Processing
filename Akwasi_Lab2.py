with open("Nouns/NounsData.txt", "r", encoding="utf-8") as f:
    data = f.readlines()

with open("Nouns/NounsIndex.txt", "r", encoding="utf-8") as f:
    indexes = f.readlines()

# Requirement #1
print("Requirement #1")
max_length = 0  # Initialised the maximum length to be "0"

# iterating over each item in the `indexes` list. For each item, it splits the item using
# the "|" character as the delimiter and selects the first part of the split result
# (`item.split("|")[0]`). Then, it replaces any underscores ("_") in the resulting string with spaces
# using the `replace()` method. Finally, it splits the string into a list of words using spaces as the
# delimiter (`n_grams.split(" ")`).
for item in indexes:
    n_grams = item.split("|")[0]
    n_grams = n_grams.split("_")
    # n_grams = n_grams.split(" ")

    if len(n_grams) >= max_length:
        max_length = len(n_grams)
        long_ngram = item.split("|")[0]

print(max_length, long_ngram)  # Prints the last item with the largest number of N-grams

# Requirement #2
print("\n\n Requiremt #2")

max_key_length = 0

# iterating over each item in the `indexes` list. For each item, it splits the item using
# the "|" character as the delimiter and assigns the resulting parts to the `separation` variable.
# Then, it splits the second part of `separation` (which contains the keys) using the "," character as
# the delimiter and assigns the resulting list to the `keys` variable.
for item in indexes:
    separation = item.split("|")
    keys = separation[1].split(",")
    if len(keys) >= max_key_length:
        max_key_length = len(keys)
        n_gram = separation

# Noticed the last item in the list always had a "\n" in the string.
# this code uses "strip()" to remove the "\n" from the last item in the list
# without this, there will be a "\n" on the last item in the list
n_gram[-1] = n_gram[-1].strip("\n")

print(max_key_length, n_gram[0], n_gram[1].split(","))  # Prints the result


# Requirement #3
# The `n_gram_keys = n_gram[1].split(",")` is splitting the second part of the `n_gram` list
# (which contains the keys) using the comma (",") character as the delimiter. It assigns the resulting
# list to the variable `n_gram_keys`.

# keys taken from requirement 2 and stored in n_gram_keys
n_gram_keys = n_gram[1].split(",")

print("\n\n Requirement #3")
for index in n_gram_keys:
    for definition in data:
        if index in definition:
            print(definition.replace("|", " "))

# My outputs are not formatted the same as in the lab2 document
# However, every piece of detail is present regardless of arrangement
# this is because the n_gram_keys is not sorted in chronological order
