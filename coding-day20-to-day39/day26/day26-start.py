# list and comperehensions
import pandas

student_dic = {
    "students": ['John', 'Jane', 'Jack', 'Jill'],
    "score": [85, 92, 78, 90]
}

for (key, value) in student_dic.items():
    print(value)

studnts_dataframe = pandas.DataFrame(student_dic)
# print(studnts_dataframe)

# loop through the dataframe
for (key, value) in studnts_dataframe.items():
    print(f"{key}: {value}")

# loop through the rows of dataframe 
for (index, row) in studnts_dataframe.iterrows():
    if row.students == "Jane":
        print(row.score)