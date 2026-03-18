print("---- Fast Food Menu ----")
print("1. Sandwich")
print("2. Pizza")
print("3. Burger")

choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("You selected Sandwich")
        print("1. Veg Sandwich")
        print("2. Grilled Sandwich")
        sub = int(input("Enter your choice: "))
        
        match sub:
            case 1:
                print("You ordered Veg Sandwich")
            case 2:
                print("You ordered Grilled Sandwich")
            case _:
                print("Invalid Sandwich choice")

    case 2:
        print("You selected Pizza")
        print("1. Thin Crust")
        print("2. Cheese Burst")
        print("3. Fresh Dough")
        sub = int(input("Enter your choice: "))
        
        match sub:
            case 1:
                print("You ordered Thin Crust Pizza")
            case 2:
                print("You ordered Cheese Burst Pizza")
            case 3:
                print("You ordered Fresh Dough Pizza")
            case _:
                print("Invalid Pizza choice")

    case 3:
        print("You selected Burger")
        print("1. Veg Burger")
        print("2. Cheese Burger")
        sub = int(input("Enter your choice: "))
        
        match sub:
            case 1:
                print("You ordered Veg Burger")
            case 2:
                print("You ordered Cheese Burger")
            case _:
                print("Invalid Burger choice")

    case _:
        print("Invalid main menu choice")