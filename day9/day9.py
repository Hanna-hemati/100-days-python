#dictionaries in python

programing_dic = {
    "bug": "an error in program taht prevents the program from running as expected",
    "function": " a pice of code that you can easily call over and over again",
    "loop": "the action of doing sth over and over again"
}

print(programing_dic["bug"])

empty_dic = {}

#wipe an existing dictionary
# programing_dic = {}
# print(programing_dic)


#edit an item in dic

# programing_dic["bug"] = "lalalla"
# print(programing_dic)

#loop
for thing in programing_dic:
    print(thing)