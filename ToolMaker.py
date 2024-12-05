def getAssignmentsPercentages():
    assignmentGradesList = []
    times = 1
    while times <= 6:
        print("What was the percent grade for Assignment", times, "? ")
        grade = int(input())
        assignmentGradesList.append(grade)
        times = times + 1
    return assignmentGradesList

def getProjectsPercentages():
    projectGradesList = []
    times = 1
    while times <= 2:
        print("What was the percent grade for Project", times, "? ")
        grade = int(input())
        projectGradesList.append(grade)
        times = times + 1
    return projectGradesList

def getAchievementsPercentages():
    achievementGradesList = []
    times = 1
    while times <= 5:
        print("What was the percent grade for Achievement", times, "? ")
        grade = int(input())
        achievementGradesList.append(grade)
        times = times + 1
    return achievementGradesList

def getFinalGrade():
    print("What was the percent grade for the Final: ")
    finalExam = int(input())
    return finalExam

def calculateWeightGrade(assignmentGrades, projectGrades, achievementGrades, finalExam):
    weightedGrade = (.20 * (assignmentGrades[0] + assignmentGrades[1] + assignmentGrades[2] +
                            assignmentGrades[3] + assignmentGrades[4] + assignmentGrades[5]))
    weightedGrade = weightedGrade + (.70 * (projectGrades[0] + projectGrades[1]))
    weightedGrade = weightedGrade + (.05 * (achievementGrades[0] + achievementGrades[1] + 
                                           achievementGrades[2] + achievementGrades[3] +
                                           achievementGrades[4]))
    weightedGrade = weightedGrade + (.05 * finalExam)
    weightedGrade = weightedGrade / (.20 * 6 + .70 * 2 + .05 * 5 + .05)
    return round(weightedGrade, 2)

def printLetterGrade(weightedGrade):
    print(f"Your final Grade is: {weightedGrade}%")
    if (weightedGrade >= 90):
        print("You got an A")
    elif (weightedGrade >= 80):
        print("You got a B")
    elif (weightedGrade >= 70):
        print("You got a C")
    elif (weightedGrade >= 60):
        print("You got a D")
    else:
        print("You got an F")


def main():
    assignmentGrades = getAssignmentsPercentages()
    projectGrades = getProjectsPercentages()
    achievementGrades = getAchievementsPercentages()
    finalExam = getFinalGrade()
    weightedGrade = calculateWeightGrade(assignmentGrades, projectGrades, achievementGrades, finalExam)
    printLetterGrade(weightedGrade)


main()