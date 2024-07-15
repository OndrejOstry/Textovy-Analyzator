'''

projekt_1.py: první projekt do Engeto Online Python Akademie

author: Ondřej Ostrý
email: ondrejostry@gmail.com
discord: ondrejostry

'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

#UŽIVATELÉ
users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
username = input("username:")
password = input("password:")

text_splitter = ("-"*40)
#PODMÍNKA VSTUPU
if username in users and users[username] == password:
    print(text_splitter)
    print("welcome to the app,",username)
    print("We have 3 text to be analyzed.")
    print(text_splitter)
    chosen_number = input("Enter a number btw. 1 and 3 to select:")
    chosen_text = TEXTS[int(chosen_number) - 1]
    print(text_splitter)

#POČET SLOV V TEXTU
    total_words = chosen_text.split()
    print("There are",len(total_words),"words in the selected text.")

    words = chosen_text.split()
    total_title = 0
    total_upper = 0
    total_lower = 0
    total_numeric = 0
    total_numsum = 0

#POČET SLOV ZAČÍNAJÍCÍCH VELKÝMI PÍSMENY
    for word in words:
        if word.istitle():
            total_title += 1
    print("There are",total_title,"titlecase words.")

#POČET SLOV NAPSANYCH VELKÝMI PÍSMENY
    for word in words:
        if word.isupper() and word.isalpha():
            total_upper += 1
#POČET SLOV NAPSANYCH MALÝMI PÍSMENY
        elif word.islower():
            total_lower += 1
#POČET NUMERICKÝCH STRINGŮ + SUMA VŠECH ČÍSEL       
        elif word.isnumeric():
            total_numsum += int(word)
            total_numeric += 1
   
#VÝPISY   
    print(f"""There are {total_upper} uppercase words.
There are {total_lower} lowercase words.
There are {total_numeric} numeric strings.
The sum of all the numbers {total_numsum}
{text_splitter}""")

#SLOUPCOVÝ GRAF
    lengths = {}
    for word in words:
        length = len(word.strip(".,"))
        if length in lengths:
            lengths[length] += 1
        else:
            lengths[length] = 1

    max_length = max(lengths.values())
    
    print("LEN|  OCCURENCES  |NR")
    print(text_splitter)
    for length in sorted(lengths):
        print(f"{length:>3}|{'*' * lengths[length]:<{max_length}}|{lengths[length]}")

else:
    print("unregistered user, terminating the program..")
    