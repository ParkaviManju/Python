class practice():  
    def subFields():
        AI = ["Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
        print("Sub-fields in AI are:")
        for i in AI:
            print(i)

    def OddEven(num):
        if(num%2 == 0):
             message = num,": is Even number"
        else:
            message = num,": is odd Number"
        return message

    def eliglible():
        Gender = input("Enter Gender:")
        Age = int(input("Enter Age:"))
        if(Gender == "Male" and Age <= 18):
            message = "Not Eligible"
        elif(Gender == "Male" and Age > 18):
            message = "Eligible"
        elif(Gender == "Female" and Age <= 18):
            message = "Not Eligible"
        elif(Gender == "Female" and Age > 18):
            message = "Eligible"   
        return message

    def percentage():
        Subject1 = int(input("Subject1:"))
        Subject2 = int(input("Subject2:"))
        Subject3 = int(input("Subject3:"))
        Subject4 = int(input("Subject4:"))
        Subject5 = int(input("Subject5:"))
        Total = Subject1 + Subject2 + Subject3 + Subject4 + Subject5
        print("Total :",Total)
        print("Percentage :", Total/5)

    def triangle():
        Height = int(input("Enter height:"))
        Breadth = int(input("Enter Breadth:"))
        print("Area Formula = (Height * Breadth)/2")
        print("Area of Triangle" ,(Height * Breadth)/2)
        Height1 = int(input("Enter height1:"))
        Height2 = int(input("Enter height2:"))
        Breadth1 = int(input("Enter Breadth1:"))
        print("Perimeter Formula = Height1 + Height2 + Breadth1")
        print("Perimeter of Triangle:", Height1 + Height2 + Breadth1)



    
