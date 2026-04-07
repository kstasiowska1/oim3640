# Read entire file
with open('data/words.txt') as f:
    text = f.readlines()

# Read line by line (best for large files)
with open('data/words.txt') as f:
    for line in f:
        print(line.strip())  # strip() removes \n

# Write to file ('w' = overwrite, 'a' = append)
with open('output.txt', 'w') as f:
    f.write('Hello, World!\n')
