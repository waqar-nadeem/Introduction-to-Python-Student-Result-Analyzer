total_marks = 0
subjects = 8

for i in range(0, subjects):
    marks = int(input("Enter marks for subject {}: ".format(i + 1)))
    total_marks = total_marks + marks

average = total_marks / subjects
print("Average marks =", average)
