msg = input("> ")
words = msg.split(' ')

emojis = {
    ":)": "\N{slightly smiling face}",
    ";)": "\N{winking face}"
}

output = ""
for word in words:
    output += emojis.get(word, word) + " "

print(output)

# Hi Abhinay ;) . How are you :) . What are you learning today.