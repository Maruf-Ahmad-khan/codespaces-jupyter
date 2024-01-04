# assign a message to a variable , and then print that message.
message = "Hello , I hope you are fine and doing well"
print(message)

# Assign a message to a variable , and print that message.
# Then change the value of the variable to a new message, and print
# the new message

message_1 = "Hi, Everyone Happy new year"
print(message_1)

message_1 = "I hope this year would be the greate year for us."
print(message_1)

# title() method change the first letter of each word to capital letter
name = "i am maruf khan"
result = name.title()
print(result)

# upper() and lower() method
print(name.upper())
print(name.lower())

# Using variable in String
first_name = 'Maruf'
last_name = 'khan'
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}")

# for python 3.5 use format()
First_Name = "Ahmad"
Last_Name = "Khan"
Full_Name = "{} {}".format(First_Name, Last_Name)
print(Full_Name)


# Adding Whitespace to String with Tabs or Newlines
print("\t Python")
print("Language: \n\tPython\n\tC\n\tJavascript")

# Striping Whitespaces
Favorite_Language = " Python"
print(Favorite_Language)
print(Favorite_Language.strip())

# Personal Messege
Personal_Message = "Eric"
Text = "Hello {},would you like to learn some Python today ?".format(Personal_Message)
print(Text)

# Famous Quotes
Quotes = "Albert Einstein once said, \"A Person who never made a mistake never tried anything new\""
print(Quotes)

# List
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
mess = f"My first bicycle was a {bicycles[0].title()}"
print(mess)