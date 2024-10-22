bmi=0
def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

#Add code here to calculate BMI
    bmi = weight/(height*height)

calculate_bmi(weight=100, height=1.65)

if(bmi<18.5):

    print("skinny bitch")

elif(bmi<=18.5 and bmi<=25.0):

    print("good")

elif(bmi>25.0):

    print("Wah fat sia")

 

