#Author: David Lemmons
#File Name: DeansList-HonorRoll.py
#Description:
#This application will allow for the user to input a student's last name or "zzz" to exit the program. If "zzz" is not entered, the program
#will continue to ask the student's first name and GPA. The program then takes the student's GPA and determines whether or not the student
#made the Dean's List, Honor Roll, or needs to study more. Then the program repeats until the user exits by entering zzz as the student's
#last name. The "study more" response was not requested for this app but was added as a response to handle GPAs under 3.25



def qualify():

    while True:
        lname = input("Enter the student's last name or 'zzz' to quit: ")

        if lname =='zzz':
            print("Goodbye!")
            break

        fname = input("Enter student's first name: ")

        while True:
            try:
                gpa = float(input("Enter student's GPA: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number for the GPA.")

        if gpa >= 3.5:
            print(fname+ " "+lname+ " has made the Dean's List!")
        elif gpa >= 3.25:
            print(fname+ " "+lname+ " has made the Honor Roll!")
        else:
            print(fname+ " "+lname+ " should study more and has not made the Honor Roll or Dean's List")

qualify()