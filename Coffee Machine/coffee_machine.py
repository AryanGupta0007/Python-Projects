import sys


class Coffee:
    def __init__(self, cost, ingredients) -> None:
        self.cost = cost
        ingredients = ingredients.split(', ')
        self.water = int(ingredients[0])
        self.milk = int(ingredients[1])
        self.coffee = int(ingredients[2])

    def __str__(self):
        return (f"cost = {self.cost}\nMilk = {self.milk}\nWater = {self.water}\nCoffee = {self.coffee}")        



def main():

    espresso = Coffee(1.5, "50, 0, 18")
    latte = Coffee(2.5, "200, 150, 24")
    cappuccino = Coffee(1.5, "250, 100, 24")
    user_input = input("Enter would you like? (espresso/cappuccino/latte) ").lower().strip()
    money = 0
    
    resources = {"milk": 300, "water": 500, "coffee": 100}
    while (user_input != "off"):
        match user_input:
            case "cappuccino":
                cost = cappuccino.cost
            case "latte":
                cost = latte.cost
            case "espresso":
                cost = espresso.cost
            case _:
                cost = 0
        if user_input != "report":
            availability_of_resources = check_resources(user_input, espresso, cappuccino, latte, resources)
            if (availability_of_resources == 1):
                verify_amount = verify_transaction(cost)
                if (verify_amount == True):
                    update_resources(user_input, espresso, cappuccino, latte, resources)
                    print(f"Here is your {user_input} enjoy!")
            else:
                sys.exit("Sorry! this machine doesn't have enough resources to fulfil your order")
            cost_list = { # contains the list of rate of different coffee's 
                "latte":latte.cost, 
                "cappuccino": cappuccino.cost, 
                "espresso":espresso.cost
                }
            lst = ["latte", "cappuccino", "espresso"]    
            
            if  user_input in lst:
                money += cost_list[user_input]
                
        else:
            print(f"Money made: ${money}\n{resources['milk']} ml milk left\n{resources['water']} ml water left\n{resources['coffee']} g coffee left ")            
        
            
        user_input = input("Enter what do you want to order ").lower().strip()
        

def verify_transaction(cost):
    """This function verifies if the user has inserted enough coins in the machine"""
    print("Please insert coins")
    dimes = int(input("how many dimes? "))
    pennies = int(input("how many pennies? "))
    quarters = int(input("how many quarters? "))
    nickels = int(input("how many nickels? "))
    
    Dimes = 0.10
    Pennies = 0.01
    Nickels = 0.05
    Quarters = 0.25
    total = dimes * Dimes + pennies * Pennies + nickels * Nickels + quarters  * Quarters
    
    if (total < cost):
        print("Not enough money and money refunded")
    elif (total > cost):
        change = total - cost
        print(f"Here is your {change} in change")
        return True
    else:
        return True

def check_resources(user_input, espresso, cappuccino, latte, resources):
    """This function checks if machine contains the right amount of  resources to serves the  coffee user wants"""
    
    match user_input:
        case "espresso":
            list_resources = ["milk", "water", "coffee"] #contains the ingredients of the coffee
            list_recipe = [espresso.milk, espresso.water, espresso.coffee] # contains the amount of ingredients for the coffee
      
            for x in range(0, 3):
                
                if(int(resources[list_resources[x]]) < int(list_recipe[x])):
                    
                    return 0

            else:
                return 1        
        case "latte":
            list_resources = ["milk", "water", "coffee"]
            list_recipe = [latte.milk, latte.water, latte.coffee]
            for x in range(0, 3):
                
                if (resources[list_resources[x]] < list_recipe[x]):
                    return 0

            else:
                return 1

        case "cappuccino":
            list_resources = ["milk", "water", "coffee"]
            list_recipe = [cappuccino.milk, cappuccino.water, cappuccino.coffee]
            for x in range(0, 3):
                
                if(resources[list_resources[x]] < list_recipe[x]):
                    return 0

            else:
                return 1
            
            
        
        case "off":
            sys.exit()

        case "report":
            pass
       
        case _:
            sys.exit("Sorry this machine doesn't offer your desired coffee")


def update_resources(user_input, espresso, cappuccino, latte, resources):
    """This function updates the resources in the coffee machine after it serves a coffee"""
    
    match user_input:
        case "espresso":
            
            list_resources = ["milk", "water", "coffee"] 
            
            list_recipe = [espresso.milk, espresso.water, espresso.coffee]
            for x in range(0, 3):
                resources[list_resources[x]] -= list_recipe[x]
                
        case "latte":
            list_resources = ["milk", "water", "coffee"]
            list_recipe = [latte.milk, latte.water, latte.coffee]
            for x in range(0, 3):
                
                resources[list_resources[x]] -= list_recipe[x]
          
        case "cappuccino":
            list_resources = ["milk", "water", "coffee"]
            list_recipe = [cappuccino.milk, cappuccino.water, cappuccino.coffee]
            for x in range(0, 3):
                resources[list_resources[x]] -= list_recipe[x]
                
        
  
if __name__ == "__main__":
    main()