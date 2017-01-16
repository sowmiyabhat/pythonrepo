message="Hello Pycharm!!!"
print(message)

# Title methods

heading = "alice in the wonderland"
print(heading.title())

heading = "dAvid copperfield"
print(heading.title())

# lowercase & upper

caption = "aLL is WElL"
print(caption.lower())
print(caption.upper())


# concatenation

firstname = "sowmiya"
lastname = "Bhat"
complete_sentence = " Hello " + firstname.title() + " " + lastname + " " + caption.upper() + "!!! "
print(complete_sentence)

# lstrip,rstrip & strip

print(complete_sentence.rstrip())
print(complete_sentence.strip())

# tabs & newline

greeting = "Hello " +firstname + " " +lastname + "." "\nGood Morning !!!"
Languages = "You know the following Languages : \n\tEnglish\n\tHindi\n\tTamil\n\tMalayalam"

sent = greeting.strip() + "\n" + Languages
print(sent)

