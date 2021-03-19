'''
 Name: Mustafa Can AYDIN
 Compile Status: Compiling
 Program Status: Working
 Notes: I have written and tested this code in Python 3.8.7 using MacOS Big Sur version 11.2.3
'''
import json

with open('response.json') as data_file:
    response = json.load(data_file)

lines = []
mp_of_word_to_lineNum = {}

for i in range(len(response)):
    lines.append("")
del response[0]

for item in response:
    upperleft_coordinate_y = item['boundingPoly']['vertices'][0]['y']
    mp_of_word_to_lineNum[item['description']] = ((upperleft_coordinate_y - 88) // 24)
    key = item['description']
    lines[mp_of_word_to_lineNum[key]] = lines[mp_of_word_to_lineNum[key]] + key + " "

string = ""
for i in lines:
    if i != "":
        string = string + i + "\n"

file1 = open('output.txt', 'w')
file1.write(string)
file1.close()
print(string)
