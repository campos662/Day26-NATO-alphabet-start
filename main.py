import pandas as pd

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv").to_dict("list")

letras = data["letter"]
nato = data["code"]

code_by_letter = {letras[i]: nato[i] for i in range(len(letras))}

#print(code_by_letter)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def translator():
    word = list(input("What's the word? ").upper())
    try:
        translation = [code_by_letter[n] for n in word]
    except KeyError:
        print("Please, type only letters!!")
    else:
        print(translation)
    finally:
        translator()
translator()

