
import sys
import random


if sys.argv[1] =="help":
    print("There is a list of CS courses; however, some courses cannot take to gether. Enter `python courses.py cscourses.txt constraints.txt` in the command line to run the program. The program will ask you enter a number of courses you would like to take and will return the courses that do not conflict each other")

def exception_handler(exception_type, exception, traceback):
    print ("Type to run: `python courses.py cscourses.txt constraints.txt`" )
sys.excepthook = exception_handler 

run=True

while run:
    def file2courses(filename):
        return open(filename).read().split("-")
    
    
    def file2constraints(filename):
        constraintList=[]
        for line in open(filename).readlines():
            constraint = line.strip().split("-")
            constraintList.append(constraint)
        return constraintList
    
    
    course = file2courses(sys.argv[1])
    constraintList= file2constraints(sys.argv[2])
    c1=""
    c2=""


    while True:
        try:
            print("How many courses would you like to take?")
            num = int(input())
        except ValueError:
            print("Please enter a valid number!")
            continue
        if num > len(course):
            print("Please enter a number smaller than", len(course))
            continue
        else:
            break
            
    while True:
        try:
            for i in range(num):
                pick = random.choice(course)
                for i in constraintList:
                    for z in i:
                        c1 = i[0]
                        c2 = i[1]
                    P2=course    
                    for x2 in P2:
                        if x2 == pick:  
                            P2.remove(x2)
                        if pick==c1 and x2==c2: 
                            P2.remove(x2)
                        if pick==c2 and x2==c1:
                            P2.remove(x2)
                print("Course Picked: ",pick)
        except Exception:
            print("No more qualified courses!")
            break
        else:
            break
    again=str(input("Do you want to search again? Type yes or no: "))
    if again != "yes":
        play = False
        print("Goodbye!")
        break
     
