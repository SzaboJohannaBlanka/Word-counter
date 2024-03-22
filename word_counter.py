def count(text):

    word = text.split()
    return len(word)

text = input("Enter some text: ")

words = count(text)

print(f"Word count: {words}")