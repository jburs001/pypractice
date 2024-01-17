"""
Title: Grade Determination Program.
Author: Jon Burstein
Details: This is a python program to determine exam, project and lab grades for students.
It teachs if/else/elif statements.
"""


exam = input("Please enter the exam grade: ")
exam = int(exam)
project = input("Please enter the project grade: ")
project = int(project)
lab = input("Please enter the lab grade: ")
lab = int(lab)

#Find each case for highest and lowest grades
if (exam > project and exam > lab and project > lab):
    print(f"Your highest grade is exam at {exam}%")
    print(f"Your lowest grade is lab at {lab}%")
elif (exam > project and exam > lab and lab > project):
    print(f"Your highest grade is exam at {exam}%")
    print(f"Your lowest grade is project at {project}%")
elif (exam > project and project == lab):
    print(f"Your highest grade is exam at {exam}%")
    print(f"Your lowest grade is project and lab at {project}%")
elif (exam == project and exam > lab):
    print(f"Your highest grades are exam and project at {exam}%.")
    print(f"Your lowest grade is lab at {lab}%")
elif (exam == project and exam == lab):
    print(f"Your highest grades are exam, project and lab at {exam}%")
elif (exam == lab and exam > project):
    print(f"Your highest grades are exam and lab at {exam}%")
    print(f"Your lowest grade is project at {project}%")
elif (project > exam and project > lab and exam > lab):
    print(f"Your highest grade is project at {project}%")
    print(f"Your lowest grade is lab at {lab}%")
elif (project > exam and project > lab and lab > exam):
    print(f"Your highest grade is project at {project}%.")
    print(f"Your lowest grade is exam at {exam}%.")
elif (project > exam and exam == lab):
    print(f"Your highest grade is project at {project}%")
    print(f"Your lowest grades are exam and lab at {exam}%")
elif (lab > exam and lab > project and project > exam):
    print(f"Your highest grade is lab at {lab}%.")
    print(f"Your lowest grade is exam at {exam}%.")
elif (lab > exam and lab > project and exam > project):
    print(f"Your highest grade is lab at {lab}%.")
    print(f"Your lowest grade is project at {project}%.") 
elif (lab > exam and exam == project):
    print(f"Your highest grade is lab at {lab}%.")
    print(f"Your lowest grades are project and exam at {project}%.")   
elif (project == lab and project > exam):
    print(f"Your highest grades are project and lab at {project}%.")
    print(f"Your lowest grade is exam at {exam}%.")

#Determine if failing.
if exam < 70:
    print(f"You have a grade below 70% on the exam.")
if lab < 70:
    print(f"You have a grade below 70% on the lab.")
if project < 70:
    print(f"You have a grade below 70% on the project.")
if (exam > 70 and project > 70 and lab > 70):
    print("All three grades are above 70%.")
if (exam < 70 and project < 70 and lab < 70):
    print("All three of your grades are below 70%")

#Find Average
exam_weight = 35
project_weight = 45
lab_weight = 20

current_average = (exam * .35) + (project * .45) + (lab * .20)
print(f"Your current average is {current_average}%.")