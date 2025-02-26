# Gradebook.py is a program that introduces the user to Python lists and basics.  The purpose is to organize a gradebook
# subjects and scores.

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Create list with subjects of classes I am taking.
subjects = ["physics", "calculus", "poetry", "history"]
# Create a list with grades for each class
grades = [98, 97, 85, 88]
# Combine subjects and grades into a 2D list manually
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]
print(gradebook)

# Add other classes and grades using append method
gradebook.append(["computer scence", 100])
gradebook.append(["visual arts", 93])
print(gradebook)

# Modify visual arts class to receive 5 extra credit points
gradebook[5][1] += 5

# Remove grade value in poetry class using .remove() and append to add "pass" "fail" value.
gradebook[2].remove(85)
gradebook[2].append("pass")

# Combine last semesters gradebook and gradebook into one list using concatenation
full_gradebook = gradebook + last_semester_gradebook
print(full_gradebook)
