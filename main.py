# 1 st one using split

# def split_the_sum(text):
#     num=text.split('-')
#     for i in range (0,len(num),+1):
#         print(num[i])

# split_the_sum("banana-orange-mango") 


# 2 nd sum
# def reverse_with_slicing(string):
#     print(string[::-1])  


# string = "Python"
# print("Original string:", string)
# print("Reversed string:", end=" ")
# reverse_with_slicing(string)

# 2nd method

# def reverse_with_reversed(string):
#     reversed_string = "".join(reversed(string))  
#     print(reversed_string)  


# string = "Python"
# print("Original string:", string)
# print("Reversed string:", end=" ")
# reverse_with_reversed(string)


# 3 rd sum:
# def count_consonants(text):
#     vowels = "aeiouAEIOU"  # all vowels
#     count = 0

#     for i in range(0,len(text),+1):
#         if text[i].isalpha() and text[i] not in vowels:  # check if letter and not vowel
#             count += 1

#     print("Number of consonants:", count)


# count_consonants("Hello World")

# 4th sum

def remove_spaces(text):
    result = ''

    for i in range(0,len(text),+1):
        if text[i] != " ":  
            result = result + text[i] 
    print(result)  



remove_spaces("python is good")

# 5th sum

def check_password(password):
    special_characters = "!@#$%^&*"
    
    
    if len(password) < 8:
        print("Password is not strong")
        return
    
    
    has_special = False
    for i in range(0,len(password),+1):
        if password[i] in special_characters:
            has_special = True
            break
    
    if has_special:
        print("Password is strong")
    else:
        print("Password is not strong")



check_password( input("enter password"))











