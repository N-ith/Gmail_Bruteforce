from itertools import product

min = 2 #set the minimun length of your password
max = 2 #set the maximum length of your password
counter = 0
character = "alohell99l" #input any information about your password. example:
# character = "hello" , it will start to shuffle the word hello and get "hello, elloh, llohe, lohel, ..."
# character = ["hello", "apple", "1"] , it will shuffle these words and get "helloapple1, applehello1, ..."
# Note: the way it shuffles depends on the max and min that u set above 

file_open = open("", 'w')

for i in range (min, max+1):
    for j in product(character, repeat=i):
        word = "".join(j)
        file_open.write(word)
        file_open.write('\n')
        counter += 1
print(f"Wordlist of {counter} passwords has been created.")     

file_open.close()
