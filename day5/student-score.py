student_score = [18, 13, 4,1 ,6, 18, 8,20 , 20, 19]

# total_exam_score = sum(student_score)
# print(total_exam_score)
#
# sum = 0
# for score in student_score:
#     sum += score
#     print(sum)
print(max(student_score))

maximum = 0
for max_score in student_score:
    if max_score > maximum:
        maximum = max_score
    print(maximum)
