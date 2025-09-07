'''
this is a csv file with student marks.
'''
with open("student_marks.csv", "rt") as f:
    text = f.read().strip()
    text = text.replace(',',' ')
    print(text)
    f.close()    