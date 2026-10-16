class collegeAssistant:
    def __init__(self):
        print('Hello, this is a program to assist you with your college tasks.')

    def calcGrade(self):
        d = {}
        lst = []
        lst1 = []
        while True:
            programStatus = input('End the program: ')
            if programStatus == 'yes' or programStatus == 'Yes':
                print('Program is now ending.')
                break
            elif programStatus == 'no' or programStatus == 'No':
                try:
                    className = input('Enter your class name: ')
                    score = int(input('Enter the score of the assignment: '))
                    percent = int(input('Enter the percent of the assignment: '))
                    d[className] = score
                    lst.append(percent/100)
                    lst1.append(percent)
                except ValueError:
                    print('Enter a proper answer.')
            else:
                print("Provide one of these: 'Yes' or 'No'")

        i=0
        count=0
        for key in d:
            count+=(d[key]*lst[i])
            i+=1
        
        total = 0
        for percentage in lst1:
            total+=percentage
        
        finalGrade = (count/percentage)*100
        
        print('Your final grade is', finalGrade)

    def calculator(self):
        while True:
            mode = input('Enter a mode (ex. add, subtract, multiply, divide): ')
            if mode == 'add':
                num1 = int(input('Enter the first number: '))
                num2 = int(input('Enter the second number: '))
                calc = num1+num2
                print("The answer is: ",calc)
            elif mode == 'subtract':
                num1 = int(input('Enter the first number: '))
                num2 = int(input('Enter the second number: '))
                calc = num1-num2
                print('The answer is:',calc)
            elif mode == 'multiply':
                num1 = int(input('Enter the first number: '))
                num2 = int(input('Enter the second number: '))
                calc = num1*num2
                print('The answer is: ',calc)
            elif mode == 'divide':
                num1 = int(input('Enter the first number: '))
                num2 = int(input('Enter the second number: '))
                calc = num1/num2
                print('The answer is: ',calc)
            else:
                print('Program is ending')
                break


mode = input('Enter a mode: ')
if mode == 'gradeCalc':
    ca = collegeAssistant()
    ca.calcGrade()

elif mode == 'calculator':
    ca = collegeAssistant()
    ca.calculator()