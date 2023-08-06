letter = '''Dear , <|Name|>,
you are selected

Date : <|Date|> '''
name = input("Enter your name:\n ")
Date = input("enter date: \n")
letter = letter.replace("<|Name|>", name)
letter = letter.replace("<|Date|>", Date)
print (letter)