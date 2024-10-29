bmi = 0

def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    # Calculate and return BMI
    bmi = weight / (height * height)

    if bmi < 18.5:
         return -1

    elif 18.5 <= bmi <= 25.0:
         return 0
   
    elif bmi > 25.0:
         return 1
    
    # Assign the returned BMI to the global variable
result = calculate_bmi(weight=100, height=1.65)

if result==-1:
     print("skinny")
elif result==0:
     print("good")
elif result==1:
     print("fat sia")

 

  
   
