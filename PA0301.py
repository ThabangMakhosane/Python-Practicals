# Writing to a new file (or overwriting an existing one)
with open("output.txt", "w") as file:
    file.write("Hello, World!")
    file.write("This is a line of text in Python.")

# Appending text to the end of an existing file
with open("output.txt", "a") as file:
    file.write("This line is appended to the file.")
