class MultiFuncations:
    def Subfields():
        subfields = ["Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
        print("Sub-fields in AI are:")
        for field in subfields:
            print(field)

    def OddEven():
        number = int(input("Enter a number:"))
        if number % 2 == 0:
            print(number, "is Even number")
        else:
            print(number, "is Odd number")
            
    def Elegible():
        gender = input("Your Gender: ").strip().lower()
        age = int(input("Your Age: "))
        if gender == 'male' and age >= 21:
            print("ELIGIBLE")
        elif gender == 'female' and age >= 18:
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")

    def percentage():
        marks = [96, 80, 80, 94, 98]
        total = 0
        for i, mark in enumerate(marks, start=1):
            print(f"Subject{i}={mark}")
            total = mark + total
        print("Total: ", total)
        print("Percentage :", (total / 500) * 100)

    def Area():
        height = int(input("Height:"))
        breadth = int(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2")
        area = (height * breadth) / 2
        print("Area of Triangle:", area)

    def Perimeter():
        height1 = int(input("Height1:"))
        height2 = int(input("Height2:"))
        breadth = int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        perimeter = height1 + height2 + breadth
        print("Perimeter of Triangle:", perimeter)