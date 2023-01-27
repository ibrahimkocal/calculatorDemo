transaction = int(input("How many transactions will you make?: "))
numbersList = []
for x in range(1, transaction + 1):
    number = int(input(f"Enter the {x}st number:"))
    numbersList.append(number) 

class Calculator():
    
    def total(self, numbersList):
        self.total = sum(numbersList)
        return self.total

    def extraction (self, numbersList):
        self.result = numbersList[0]

        for i in range(1, len(numbersList)):
            self.result -= numbersList[i]
        return self.result
                        
    def multiplication(self, numbersList):
        self.result = 1
        for x in numbersList:
            self.result = self.result * x 
        return self.result

    def division(self, numbersList):
        self.result = numbersList[0]

        for i in range(1, len(numbersList)):
            self.result /= numbersList[i]
        return self.result

    def average(self, numberList):
        self.total = sum(numberList)
        avg = self.total / len(numberList)
        return avg   


calculator = Calculator()

while True:
    print(" CALCULATOR ".center(30, "*"))
    result = input("1- Total\n2- Extraction Process\n3- Multiplication\n4- Division\n5- Average\n6- Exit\nEnter the number of the transaction you want to do (ex:1, ex:2): ")
    if result == "6":
        break
    elif result == "1":
        print(f"Result:  {calculator.total(numbersList)}")   
    elif result == "2":
        print(f"Result:  {calculator.multiplication(numbersList)}")  
    elif result == "3":
        print(f"Result:  {calculator.extraction(numbersList)}")  
    elif result == "4":
        print(f"Result:  {calculator.division(numbersList)}")
    elif result == "5":
        print(f"Result:  {calculator.average(numbersList)}")
    else:
        print("Error! You have made an incomplete or incorrect operation. Try again.")

