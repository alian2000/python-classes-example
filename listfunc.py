list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
element = 10
print (list_numbers.index(element)) # find index position of number 10
print (list_numbers.index(10))  # give me the position of the value
print (list_numbers[9])   #valuse in position 9
print (len(list_numbers))   # watch how to use the length function

input = ['Python', 'Java', 'Ruby', 'JavaScript']
size = len(input)
print(size)
print (input.index("Java"))
print (input[3].upper())
for language in input:
    print (language)
    print(language.lower())
for prog in input:
    if prog=="Python":
        print("we are learning "+ prog+"  now" )
    else:
        print("learn "+prog+" in the future")
        print (prog)
        print(prog.lower())
        
myscore=100
message= "i scored %s points"
print(message % myscore)