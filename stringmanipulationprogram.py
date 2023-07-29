#Week Two(2)  Python Assignment
#Name: Ransford Addai
#Training ID: 32524




#QUESTION ONE(1)
#Prompt the user to enter a string
input_string = input("Please enter a string: ")

#Check if the user entered an empty string or only white space characters
if not input_string:
    print("You entered an empty string. Please enter characters next time.")
else:
    #reverse the string and input the result
    reversed_string = input_string[::-1]
    print("Reversed string: ", reversed_string)



#QUESTION TWO()
#Find the longest word in the input string and print it.
words = input_string.split()
longest_word = max(words, key=len)
print("Longest word: ", longest_word)



#QUESTION THREE(3)
#Find the shortest word in the input string and print it
shortest_word = min(words, key=len)
print("Shortest word: ", shortest_word)



#QUESTION FOUR(4)
#Count the occurences of a specific character in the input string and print the count
character_to_search = input("Please enter a character to count: ")
caracter_count = input_string.count(character_to_search)
print(f"Occurences of '{character_to_search}' in the input sting: {caracter_count}")











