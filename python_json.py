'''
Python program to read and parse json file that uses mixed
and nested Dictionaries and Arrays, hey David, enjoy!

JSON OBJECT     PYTHON OBJECT       SYMBOL
object          dict                {}
array           list                []
'''

import json

# function to separate print statements
def separate():
    print("\n==============================================\n")
 
# Opening JSON file
f = open('post_result.json')
 
# returns JSON object as a dictionary
result = json.load(f)
separate()
 
# print entire result
print("printing result:" + str(result))
separate()

# format and print json
result_formatted_str = json.dumps(result, indent=2)
print("printing result_formatted_str:" + str(result_formatted_str))
separate()

# get hobbies OBJECT/DICTIONARY
hobbies = result["hobbies"]
print("hobbies: " + str(hobbies))
separate()

# get indoors hobbies LIST/ARRAY, array inside a dictionary
hobbies_indoors = result["hobbies"]["indoors"]
print("hobbies_indoors: " + str(hobbies_indoors))
separate()

# THINGS GET INTERESTING, accessing nested values
separate()

# get 9 mm LIST/ARRAY, it is:
#   inside a 'guns' DICTIONARY
#       inside 'outdoors' DICTIONARY
#           inside 'hobbies' DICTIONARY
nine_mm_guns = result["hobbies"]["outdoors"]["guns"]["9 mm"]
print("nine_mm_guns: " + str(nine_mm_guns))
separate()

# get 9 mm for concealed carry, access second item in ARRAY
nine_mm_conealed = result["hobbies"]["outdoors"]["guns"]["9 mm"][1]
print("should be the x macro: " + str(nine_mm_conealed))
separate()

# EVEN MORE INTERESTING mix ARRAY and DICTIONARY
# get author of New Testament "Paul", it is
#   inside 'new_testament' ARRAY  ->  4th item index is 3
#       inside 'Apostles' DICTIONARY  ->  key is "new_testament"
#           inside 'friends' ARRAY  -> 3rd item index is 2
#               inside main 'result' DICTIONARY  ->  key is "friends"
new_test_author = result["friends"][2]["Apostles"]["new_testament"][3]
print("new_test_author: " + str(new_test_author))
separate()

# Closing file
f.close()
